"""
intake.py - Run the full Calling Card intake from 4 URLs.

This is the entry point. Give it the company URL, JD URL, and founder LinkedIn
and it scaffolds the card folder, captures screenshots, detects their stack,
and writes research notes ready for me (Claude) to draft the brief.

Usage:
    python intake.py <slug> --company <url> --jd <url> --founder <url> [--call-date YYYY-MM-DD]

Example:
    python intake.py scispace \\
        --company https://scispace.com/ \\
        --jd https://wellfound.com/jobs/9999999-senior-ai-pm \\
        --founder https://www.linkedin.com/in/saikiranchandha/ \\
        --call-date 2026-05-15

Output:
    cards/<slug>/
    +-- shots/<slug>-home.png       (best-effort)
    +-- _research/
        +-- intake.md               (the inputs you provided)
        +-- stack.txt               (marketing stack detected)
        +-- raw-html.html           (homepage HTML for manual scanning)
        +-- README.md               (research-status checklist)
"""

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

import argparse
import datetime as dt
import shutil
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)

ROOT = Path(__file__).resolve().parent.parent
CAPTURE = Path(__file__).resolve().parent / "capture_site.py"
DETECT = Path(__file__).resolve().parent / "detect_stack.py"


def step(label: str):
    print()
    print("=" * 64)
    print(f"  {label}")
    print("=" * 64)


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def slugify(s: str) -> str:
    return "".join(c.lower() if c.isalnum() else "-" for c in s).strip("-")


def fetch_raw_html(url: str, out_path: Path):
    """Save the raw HTML; not used for rendering, but lets me grep for clues."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="ignore")
        out_path.write_text(html, encoding="utf-8")
        return len(html)
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  ! couldn't fetch HTML: {e}")
        return 0


def run_capture(slug: str, url: str, suffix: str = "home", full: bool = False) -> bool:
    cmd = [sys.executable, str(CAPTURE), slug, url, "--suffix", suffix]
    if full:
        cmd.append("--full")
    try:
        result = subprocess.run(cmd, capture_output=False)
        return result.returncode == 0
    except subprocess.SubprocessError as e:
        print(f"  ! capture failed: {e}")
        return False


def run_detect(url: str, out_path: Path) -> bool:
    cmd = [sys.executable, str(DETECT), url, "--out", str(out_path)]
    try:
        result = subprocess.run(cmd, capture_output=False)
        return result.returncode == 0
    except subprocess.SubprocessError as e:
        print(f"  ! detect failed: {e}")
        return False


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

INTAKE_MD_TPL = """# Intake - {slug}

**Filed:** {today}

```
COMPANY URL:        {company}
JD URL:             {jd}
FOUNDER LINKEDIN:   {founder}
CALL DATE:          {call_date}
DAYS TO DELIVER:    {days_to_deliver}
```

## What I (Claude) need to do next

1. Open the company URL and (if Microlink/thum.io captured a real screenshot)
   visually verify the saved image at `shots/{slug}-home.png`. If it's a
   403/CAPTCHA page, ask the user for a manual screenshot.
2. Read the JD verbatim from the user's message.
3. Pull founder posts / public POV from LinkedIn / search.
4. Cross-reference detected stack (`_research/stack.txt`) for Finding 10 angle.
5. Synthesize the 7-bullet brief and send to user for sign-off.
6. Only after sign-off: scaffold `cards/{slug}/` from `cards/cielo/` and
   rewrite per-finding content.
"""

RESEARCH_README_TPL = """# Research artifacts - {slug}

This folder is the working memory for the {slug} card. Nothing in here is
shipped to the user; it's just my (Claude's) notes during the intake phase.

## Files

- `intake.md`       - the four URLs you gave me + delivery deadline
- `stack.txt`       - marketing/analytics tools detected on their homepage
- `raw-html.html`   - homepage HTML I can grep through for hidden clues
- (optional) `notes.md` - any additional findings I discover during research

## Status checklist

- [{home_shot_status}] Homepage screenshot at `../shots/{slug}-home.png`
- [{stack_status}] Stack detection at `stack.txt`
- [{html_status}] Raw HTML at `raw-html.html`
- [ ] Founder POV + recent posts (manual research)
- [ ] Company stage + funding (manual research)
- [ ] ICP segments visible on homepage (manual research)
- [ ] 7-bullet brief drafted and sent to user
- [ ] User sign-off received
- [ ] Card scaffolded at `../index.html`, `../audit.html`, etc.
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="company slug, e.g. 'scispace'")
    ap.add_argument("--company", required=True, help="company homepage URL")
    ap.add_argument("--jd", default="(not provided)", help="JD URL")
    ap.add_argument("--founder", default="(not provided)", help="founder LinkedIn URL")
    ap.add_argument("--call-date", default="(not set)", help="scheduled call date (YYYY-MM-DD)")
    ap.add_argument("--also-capture", nargs="*", default=[],
                    help="extra URLs to capture, format: suffix=URL  (e.g. about=https://.../about)")
    args = ap.parse_args()

    slug = slugify(args.slug)
    card_dir = ROOT / "cards" / slug
    research_dir = card_dir / "_research"
    shots_dir = card_dir / "shots"

    today = dt.date.today().isoformat()

    # --- Step 1: Scaffold folders --------------------------------------
    step(f"1/4  Scaffolding cards/{slug}/")
    research_dir.mkdir(parents=True, exist_ok=True)
    shots_dir.mkdir(parents=True, exist_ok=True)
    print(f"  created: {card_dir.relative_to(ROOT)}/")
    print(f"  created: {shots_dir.relative_to(ROOT)}/")
    print(f"  created: {research_dir.relative_to(ROOT)}/")

    # --- Step 2: Save intake doc + raw HTML ----------------------------
    step("2/4  Saving intake + raw HTML")
    days_left = "(call_date not set)"
    if args.call_date != "(not set)":
        try:
            cd = dt.date.fromisoformat(args.call_date)
            days_left = str((cd - dt.date.today()).days)
        except ValueError:
            days_left = "(invalid date)"

    write(research_dir / "intake.md", INTAKE_MD_TPL.format(
        slug=slug, today=today,
        company=args.company, jd=args.jd, founder=args.founder,
        call_date=args.call_date, days_to_deliver=days_left,
    ))
    print(f"  intake.md written")

    raw_html_size = fetch_raw_html(args.company, research_dir / "raw-html.html")
    print(f"  raw-html.html: {raw_html_size:,} bytes")

    # --- Step 3: Capture screenshot ------------------------------------
    step("3/4  Capturing screenshots")
    home_shot_ok = run_capture(slug, args.company, suffix="home")
    extra_status = []
    for kv in args.also_capture:
        if "=" not in kv:
            print(f"  ! ignoring malformed --also-capture entry: {kv}")
            continue
        suffix, extra_url = kv.split("=", 1)
        ok = run_capture(slug, extra_url, suffix=suffix)
        extra_status.append((suffix, ok))

    # --- Step 4: Detect stack ------------------------------------------
    step("4/4  Detecting marketing/analytics stack")
    stack_ok = run_detect(args.company, research_dir / "stack.txt")

    # --- Status README -------------------------------------------------
    write(research_dir / "README.md", RESEARCH_README_TPL.format(
        slug=slug,
        home_shot_status="x" if home_shot_ok else " ",
        stack_status="x" if stack_ok else " ",
        html_status="x" if raw_html_size > 1000 else " ",
    ))

    # --- Summary -------------------------------------------------------
    print()
    print("=" * 64)
    print("  SUMMARY")
    print("=" * 64)
    print(f"  card dir:        cards/{slug}/")
    print(f"  intake doc:      cards/{slug}/_research/intake.md")
    print(f"  homepage shot:   {'OK' if home_shot_ok else 'MANUAL NEEDED'}")
    print(f"  stack detected:  {'OK' if stack_ok else 'FAILED'}")
    print(f"  raw HTML saved:  {'OK' if raw_html_size > 1000 else 'FAILED ('+str(raw_html_size)+'b)'}")
    if extra_status:
        for suf, ok in extra_status:
            print(f"  extra '{suf}':       {'OK' if ok else 'MANUAL NEEDED'}")

    print()
    print("Next: review _research/intake.md and _research/stack.txt, then ask")
    print("Claude to draft the 7-bullet brief.")


if __name__ == "__main__":
    main()
