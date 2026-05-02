"""
detect_stack.py - Detect a company's marketing/analytics/CRM/intent stack.

Curls their homepage HTML and matches against ~50 known providers. Used for
Audit Finding 10 (visitor-reveal -> outbound loop). The presence of intent
tools (Reb2b, Apollo, Clearbit, etc.) means they're paying for B2B visitor
data; the audit angle is whether they're actioning it.

Usage:
    python detect_stack.py <url>  [--out path]

Examples:
    python detect_stack.py https://www.cielo.agency/
    python detect_stack.py https://scispace.com/  --out cards/scispace/_research/stack.txt
"""

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

import re
import argparse
import urllib.request
import urllib.error
from pathlib import Path


PATTERNS = {
    # Analytics
    "Google Analytics":      r"(googletagmanager\.com/gtag|gtag\(\s*['\"]js|UA-\d+|G-[A-Z0-9]{8,})",
    "Google Tag Manager":    r"GTM-[A-Z0-9]+",
    "Plausible":             r"plausible\.io|plausible\.js",
    "Fathom":                r"usefathom\.com",
    "Simple Analytics":      r"simpleanalyticscdn\.com",
    # B2B intent / visitor identification
    "Reb2b":                 r"reb2b\.com|b2bjsstore",
    "RB2B":                  r"rb2b\.com|cdn\.rb2b\.com",
    "Apollo":                r"apollo\.io|assets\.apollo\.io",
    "Clearbit":              r"clearbit\.com",
    "ZoomInfo":              r"zoominfo\.com|ws-na\.amazon-adsystem",
    "6sense":                r"6sense\.com",
    "Demandbase":            r"demandbase\.com",
    # Product analytics / event tracking
    "Segment":               r"cdn\.segment\.com|analytics\.segment\.io",
    "Mixpanel":              r"cdn\.mxpnl\.com|api\.mixpanel\.com",
    "Amplitude":             r"cdn\.amplitude\.com|amplitude-cdn\.com",
    "Heap":                  r"cdn\.heap\.io|heapanalytics\.com",
    "PostHog":               r"posthog\.com|app\.posthog",
    # CRM / marketing automation
    "GoHighLevel":           r"highlevel|leadconnectorhq|msgsndr\.com",
    "HubSpot":               r"js\.hs-scripts\.com|forms\.hubspot\.com|hsforms\.net",
    "Marketo":               r"mktoresp\.com|marketo\.com",
    "Salesforce Pardot":     r"pi\.pardot\.com|pardot\.com",
    "ActiveCampaign":        r"activehosted\.com",
    "Mailchimp":             r"chimpstatic\.com|mailchimp\.com",
    # Chat / engagement
    "Drift":                 r"js\.driftt\.com|driftt\.com",
    "Intercom":              r"widget\.intercom\.io|intercomcdn",
    "Crisp":                 r"client\.crisp\.chat",
    "Tidio":                 r"code\.tidio\.co",
    # Session replay / heatmaps
    "Hotjar":                r"static\.hotjar\.com|insights\.hotjar",
    "FullStory":             r"fullstory\.com|edge\.fullstory",
    "Contentsquare":         r"t\.contentsquare\.net|contentsquare",
    "Microsoft Clarity":     r"clarity\.ms",
    "Smartlook":             r"smartlook\.cloud",
    "Mouseflow":             r"mouseflow\.com",
    # Visitor analytics (lighter-weight)
    "TWIPLA":                r"visitor-analytics\.io|twipla",
    # Ad pixels
    "LinkedIn Insight":      r"snap\.licdn\.com",
    "Facebook Pixel":        r"connect\.facebook\.net|fbq\(",
    "Twitter Pixel":         r"static\.ads-twitter\.com",
    "Reddit Pixel":          r"redditstatic\.com",
    "TikTok Pixel":          r"analytics\.tiktok\.com",
    "Pinterest Tag":         r"ct\.pinterest\.com",
    # Site builders / hosting
    "Wix":                   r"wixstatic\.com|wix\.com",
    "Webflow":               r"webflow\.com|website-files\.com",
    "Framer":                r"framerusercontent\.com|framer\.app",
    "Figma Make":            r"Created in Figma Make|figmake|figma\.com/make",
    "Squarespace":           r"squarespace-cdn\.com|squarespace\.com",
    "Vercel":                r"_vercel|vercel\.app",
    "Netlify":               r"netlify\.app|netlify\.com",
    "Cloudflare":            r"cloudflare|cf-ray",
    # AI / SDKs
    "Anthropic SDK":         r"anthropic|claude\.ai",
    "OpenAI":                r"openai\.com|chat\.openai",
    "Algolia search":        r"algolia\.net|algolianet\.com",
    "Stripe":                r"js\.stripe\.com|stripe\.com",
}


INTENT_TOOLS = {
    "Reb2b", "RB2B", "Apollo", "Clearbit", "ZoomInfo",
    "6sense", "Demandbase",
}


UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            charset = r.headers.get_content_charset() or "utf-8"
            return r.read().decode(charset, errors="ignore")
    except urllib.error.HTTPError as e:
        print(f"warn: HTTP {e.code} fetching {url}", file=sys.stderr)
        # Some sites 403 the bare HTML but ship inline scripts on the rendered
        # page. We can still try and read whatever response body came back.
        try:
            return e.read().decode("utf-8", errors="ignore")
        except Exception:
            return ""
    except urllib.error.URLError as e:
        sys.exit(f"error: cannot resolve {url}: {e.reason}")


def detect(html: str) -> list[str]:
    found = []
    for name, pat in PATTERNS.items():
        if re.search(pat, html, re.IGNORECASE):
            found.append(name)
    return found


def format_report(url: str, found: list[str]) -> str:
    lines = [f"Stack scan: {url}", "=" * 60]
    if not found:
        lines.append("No known marketing/analytics tools detected from raw HTML.")
        lines.append("(Many SPAs load these tools after JS executes; consider")
        lines.append(" running this on the rendered page or in browser devtools.)")
        return "\n".join(lines)

    lines.append(f"Detected ({len(found)}):")
    for name in found:
        marker = "*" if name in INTENT_TOOLS else " "
        lines.append(f"  {marker} {name}")
    lines.append("")
    intent_present = [t for t in found if t in INTENT_TOOLS]
    if intent_present:
        lines.append("AUDIT HOOK -> Finding 10:")
        lines.append(f"  Intent / visitor-ID tools detected: {', '.join(intent_present)}")
        lines.append("  They're paying for B2B visitor data already.")
        lines.append("  The leak isn't acquisition cost - it's outbound action.")
        lines.append("  Frame the finding around the missing follow-up loop.")
    else:
        lines.append("No intent / visitor-ID tools detected.")
        lines.append("Finding 10 should pivot to a different revenue lever:")
        lines.append("  e.g. retargeting pixel coverage, email capture, or")
        lines.append("  funnel-stage instrumentation gaps.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", help="optional file to write report to")
    args = ap.parse_args()

    print(f"Fetching {args.url} ...")
    html = fetch(args.url)
    print(f"Fetched {len(html):,} bytes\n")

    found = detect(html)
    report = format_report(args.url, found)
    print(report)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(f"\nReport saved: {out_path}")


if __name__ == "__main__":
    main()
