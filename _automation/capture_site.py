"""
capture_site.py - Capture screenshots of a company's website with a fallback chain.

Tries multiple screenshot services in order until one works. CloudFront /
Cloudflare protected sites often reject Microlink + thum.io but some services
(or alternate user-agent paths) get through. If everything fails, prompts the
user for a manual screenshot.

Usage:
    python capture_site.py <slug> <url> [--suffix home] [--full]

Examples:
    python capture_site.py cielo https://www.cielo.agency/
    python capture_site.py cielo https://www.cielo.agency/aboutus --suffix about
    python capture_site.py scispace https://scispace.com/ --full

Output:
    ../cards/<slug>/shots/<slug>-<suffix>.png  (resized to <= 1280x900, optimised)
"""

# Force UTF-8 stdout on Windows so we can print without UnicodeEncodeError.
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

import io
import json
import time
import argparse
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Install Pillow first:  pip install Pillow")


# Use ASCII-safe symbols on Windows where possible; Unicode is fine on stdout
# now that we reconfigured encoding above, but keep arrows minimal anyway.
ARROW = "->"


# ---------------------------------------------------------------------------
# Capture services (tried in order)
# ---------------------------------------------------------------------------

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)


def _http_get(url: str, timeout: int = 70) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def via_microlink(url: str, full_page: bool = False) -> bytes:
    """Microlink free tier. Often blocked by CloudFront."""
    qs = {
        "url": url,
        "screenshot": "true",
        "meta": "false",
        "waitFor": "5500",
        "viewport.width": "1280",
        "viewport.height": "900",
    }
    if full_page:
        qs["fullPage"] = "true"
        qs["waitFor"] = "8000"
    api = "https://api.microlink.io/?" + urllib.parse.urlencode(qs)
    print(f"  {ARROW} microlink ...")
    raw = _http_get(api)
    meta = json.loads(raw)
    if meta.get("status") != "success":
        raise RuntimeError(f"microlink reported non-success: {meta.get('statusCode')}")
    img_url = meta["data"]["screenshot"]["url"]
    png = _http_get(img_url, timeout=60)
    _validate_real_screenshot(png)
    return png


def via_thumio(url: str, full_page: bool = False) -> bytes:
    """thum.io free tier. Hits CAPTCHA on heavily-protected sites."""
    print(f"  {ARROW} thum.io ...")
    if full_page:
        endpoint = f"https://image.thum.io/get/width/1280/{url}"
    else:
        endpoint = f"https://image.thum.io/get/width/1280/crop/900/{url}"
    png = _http_get(endpoint, timeout=60)
    _validate_real_screenshot(png)
    return png


def via_pagespeed_thumb(url: str, full_page: bool = False) -> bytes:
    """
    Google PageSpeed Insights captures a real-browser screenshot of the site
    and returns it as part of its JSON. We extract just the screenshot.
    Requires no API key for limited use. Slow but reliable.
    """
    print(f"  {ARROW} PageSpeed Insights ...")
    api = (
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?"
        + urllib.parse.urlencode({"url": url, "strategy": "desktop"})
    )
    raw = _http_get(api, timeout=120)
    meta = json.loads(raw)
    audits = meta.get("lighthouseResult", {}).get("audits", {})
    final_screenshot = audits.get("final-screenshot", {}).get("details", {})
    data_uri = final_screenshot.get("data", "")
    if not data_uri.startswith("data:image"):
        raise RuntimeError("PageSpeed didn't return a screenshot")
    import base64
    b64 = data_uri.split(",", 1)[1]
    return base64.b64decode(b64)


SERVICES = [
    ("microlink", via_microlink),
    ("thum.io", via_thumio),
    ("pagespeed", via_pagespeed_thumb),
]


# ---------------------------------------------------------------------------
# Validation: did we get a real site capture or a 403/CAPTCHA page?
# ---------------------------------------------------------------------------

REJECT_HINTS = (
    "403 ERROR",
    "Request blocked",
    "Let's confirm you are human",
    "Confirm you are a human",
    "Just a moment",
    "Attention Required",
    "captcha",
    "cf-error-details",
    "access denied",
)


def _validate_real_screenshot(png: bytes):
    """
    Heuristic: render the PNG, OCR-light by sampling top region for known
    blocking-page text. If the image is suspiciously small or matches a known
    block page, raise so the next service is tried.
    """
    if len(png) < 8000:
        raise RuntimeError(f"screenshot too small ({len(png)}b) - probably an error page")
    img = Image.open(io.BytesIO(png))
    if img.size[0] < 600 or img.size[1] < 400:
        raise RuntimeError(f"screenshot too small ({img.size}) - probably an error page")
    # Convert top region to a grayscale + simple text-like check.
    # We can't OCR without tesseract, but the 403 / CAPTCHA pages tend to be
    # mostly white with concentrated dark text in the upper third. The actual
    # content of a marketing site fills the frame with imagery / colour.
    top = img.crop((0, 0, img.size[0], img.size[1] // 3)).convert("RGB")
    pixels = list(top.getdata())
    sample = pixels[::200]
    near_white = sum(1 for p in sample if p[0] > 240 and p[1] > 240 and p[2] > 240)
    if near_white > len(sample) * 0.85:
        # The top third is overwhelmingly white => likely an error/CAPTCHA page
        raise RuntimeError("screenshot looks like a blank/error page")


# ---------------------------------------------------------------------------
# Manual fallback
# ---------------------------------------------------------------------------

MANUAL_PROMPT = """
All automated capture services failed for this URL. The site is likely behind
CloudFront / Cloudflare bot protection.

Two ways forward:

  1) MANUAL: open the URL in your browser, take a 1280x900 above-the-fold
     screenshot, and save it at:

        {target}

  2) PROCEED WITHOUT SCREENSHOTS: the audit will use text-based callouts only
     (less visual impact but still ships).

Once the file exists I'll pick it up automatically. Run again to retry the
auto-capture or just continue with the build.
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def save_resized(png_bytes: bytes, out_path: Path, max_w: int = 1280, max_h: int = 900):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(png_bytes)
    img = Image.open(out_path)
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    img.save(out_path, optimize=True)
    print(f"  saved: {out_path}  ({img.size[0]}x{img.size[1]}, {out_path.stat().st_size:,}b)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="company slug, e.g. 'cielo'")
    ap.add_argument("url", help="full URL to capture")
    ap.add_argument("--suffix", default="home", help="shot suffix (home/about/portfolio/...)")
    ap.add_argument("--full", action="store_true", help="capture full scrollable page")
    ap.add_argument("--service", help="force a specific service: microlink|thum.io|pagespeed")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    out = here.parent / "cards" / args.slug / "shots" / f"{args.slug}-{args.suffix}.png"

    print(f"\nCapturing: {args.url}")
    print(f"Target:    {out.relative_to(here.parent)}\n")

    services = SERVICES
    if args.service:
        services = [(n, fn) for (n, fn) in SERVICES if n == args.service]
        if not services:
            sys.exit(f"unknown service: {args.service}  (available: microlink, thum.io, pagespeed)")

    last_err = None
    for name, fn in services:
        try:
            png = fn(args.url, full_page=args.full)
            save_resized(png, out)
            print(f"\nDone via {name}.")
            return
        except (urllib.error.URLError, RuntimeError, json.JSONDecodeError) as e:
            print(f"  ! {name} failed: {e}")
            last_err = e
            time.sleep(1)
        except Exception as e:
            print(f"  ! {name} exception: {type(e).__name__}: {e}")
            last_err = e

    print(MANUAL_PROMPT.format(target=out.relative_to(here.parent)))
    sys.exit(2)


if __name__ == "__main__":
    main()
