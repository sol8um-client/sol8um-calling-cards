"""
detect_stack.py — Curl a company's marketing HTML and detect their analytics
+ CRM + intent stack. Used for Audit Finding 10 (visitor-reveal → outbound loop).

Usage:
    python detect_stack.py https://www.cielo.agency/

Detects: GA, GTM, Reb2b, Apollo, Segment, Mixpanel, Amplitude, GoHighLevel,
HubSpot, Hotjar, FullStory, Contentsquare, Drift, Intercom, RB2B (alt name),
Clearbit, ZoomInfo, 6sense, Demandbase, TWIPLA, and several others.

The presence of Reb2b/Apollo/RB2B/etc means the company is paying for visitor
identification — a critical Finding 10 hook (the data is sunk cost; the leak
is operational).
"""

import sys
import re
import urllib.request

PATTERNS = {
    "Google Analytics":  r"(googletagmanager\.com|gtag\(|UA-\d+|G-[A-Z0-9]+)",
    "Google Tag Manager": r"GTM-[A-Z0-9]+",
    "Reb2b":             r"reb2b\.com|b2bjsstore",
    "RB2B":              r"rb2b\.com|cdn\.rb2b\.com",
    "Apollo":            r"apollo\.io|assets\.apollo\.io",
    "Clearbit":          r"clearbit\.com",
    "ZoomInfo":          r"zoominfo\.com",
    "6sense":            r"6sense\.com",
    "Demandbase":        r"demandbase\.com",
    "Segment":           r"segment\.com|cdn\.segment\.com|segment\.io",
    "Mixpanel":          r"mixpanel\.com|cdn\.mxpnl\.com",
    "Amplitude":         r"amplitude\.com|cdn\.amplitude\.com",
    "Heap":              r"heap\.io|cdn\.heap\.io",
    "GoHighLevel":       r"highlevel|leadconnectorhq|msgsndr\.com",
    "HubSpot":           r"hubspot\.com|js\.hs-scripts\.com",
    "Marketo":           r"mktoresp|marketo\.com",
    "Salesforce Pardot": r"pardot\.com|pi\.pardot",
    "Drift":             r"drift\.com|js\.driftt\.com",
    "Intercom":          r"intercom\.io|widget\.intercom\.io",
    "Crisp":             r"crisp\.chat",
    "Hotjar":            r"hotjar\.com|static\.hotjar\.com",
    "FullStory":         r"fullstory\.com|fs\.fullstory",
    "Contentsquare":     r"contentsquare|t\.contentsquare\.net",
    "Microsoft Clarity": r"clarity\.ms",
    "Smartlook":         r"smartlook\.com",
    "Mouseflow":         r"mouseflow\.com",
    "TWIPLA":            r"visitor-analytics\.io|twipla",
    "LinkedIn Insight":  r"snap\.licdn\.com",
    "Facebook Pixel":    r"connect\.facebook\.net|fbq\(",
    "Twitter Pixel":     r"static\.ads-twitter\.com",
    "Reddit Pixel":      r"redditstatic\.com",
    "TikTok Pixel":      r"analytics\.tiktok\.com",
    "Wix":               r"wix\.com|wixstatic\.com",
    "Webflow":           r"webflow\.com|website-files\.com",
    "Framer":            r"framerusercontent\.com",
    "Figma Make":        r"Created in Figma Make|figma\.com",
    "Squarespace":       r"squarespace\.com|squarespace-cdn",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="ignore")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: detect_stack.py <url>")
    url = sys.argv[1]
    html = fetch(url)
    print(f"\nFetched {len(html):,} bytes from {url}\n")

    found = []
    for name, pat in PATTERNS.items():
        if re.search(pat, html, re.IGNORECASE):
            found.append(name)

    if not found:
        print("No known marketing/analytics tools detected.")
        return

    print("Detected stack:")
    for name in found:
        print(f"  · {name}")

    print()
    intent_tools = {"Reb2b", "RB2B", "Apollo", "Clearbit", "ZoomInfo",
                    "6sense", "Demandbase"}
    has_intent = [t for t in found if t in intent_tools]
    if has_intent:
        print(f"⚠ Intent / visitor-ID tools running: {', '.join(has_intent)}")
        print("  → This means they're paying for B2B visitor data.")
        print("  → Finding 10 angle: Are they actioning it?")
        print("  → If not, that's the biggest revenue lever in the audit.")


if __name__ == "__main__":
    main()
