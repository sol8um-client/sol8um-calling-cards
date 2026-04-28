"""
capture_site.py — Capture screenshots of a company's website via Microlink.

Usage:
    python capture_site.py <company-slug> <url> [--full]
    python capture_site.py cielo https://www.cielo.agency/
    python capture_site.py cielo https://www.cielo.agency/aboutus --suffix about

Output:
    ../cards/<company-slug>/shots/<slug>-<suffix>.png  (default suffix: home)

Resizes to 1280x900 to keep the deliverable lightweight.
Microlink free tier supports ~100 captures/day.
"""

import sys
import json
import time
import argparse
import urllib.request
import urllib.parse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Install Pillow first:  pip install Pillow")


def capture(url: str, full_page: bool = False, wait_ms: int = 5000) -> bytes:
    """Returns raw PNG bytes for the URL via Microlink."""
    qs = {
        "url": url,
        "screenshot": "true",
        "meta": "false",
        "waitFor": str(wait_ms),
        "viewport.width": "1280",
        "viewport.height": "900",
    }
    if full_page:
        qs["fullPage"] = "true"
        qs["waitFor"] = str(max(wait_ms, 6000))
    api = "https://api.microlink.io/?" + urllib.parse.urlencode(qs)
    print(f"  → microlink: {url}")
    with urllib.request.urlopen(api, timeout=70) as r:
        meta = json.load(r)
    if meta.get("status") != "success":
        raise RuntimeError(f"microlink failed: {meta}")
    img_url = meta["data"]["screenshot"]["url"]
    print(f"  → downloading: {img_url}")
    with urllib.request.urlopen(img_url, timeout=60) as r:
        return r.read()


def save_resized(png_bytes: bytes, out_path: Path, max_w: int = 1280, max_h: int = 900):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(png_bytes)
    img = Image.open(out_path)
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    img.save(out_path, optimize=True)
    print(f"  → saved: {out_path}  ({img.size[0]}x{img.size[1]})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="company slug, e.g. 'cielo'")
    ap.add_argument("url", help="full URL to capture")
    ap.add_argument("--suffix", default="home", help="shot suffix (home/about/portfolio/...)")
    ap.add_argument("--full", action="store_true", help="capture full scrollable page")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    out = here.parent / "cards" / args.slug / "shots" / f"{args.slug}-{args.suffix}.png"

    png = capture(args.url, full_page=args.full)
    save_resized(png, out)
    print("\nDone.")


if __name__ == "__main__":
    main()
