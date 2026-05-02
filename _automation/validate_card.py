"""
validate_card.py - Pre-flight quality check for a card before pushing.

Catches the silent ship-stoppers: missing files, broken stylesheet refs,
unfilled template tokens, the wrong phone number, console-error patterns,
oversized images, em dashes that snuck in.

Usage:
    python validate_card.py <slug>
    python validate_card.py cielo

Exits 0 on clean. Exits 1 on any failure.
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
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_HTML = [
    "index.html",
    "audit.html",
    "morning-brief.html",
    "email-triage.html",
    "pre-meeting.html",
    "reflection.html",
]

# Things that should NEVER appear in shipped HTML
BAD_PATTERNS = [
    (r"\u2014", "em dash detected (use comma/period/colon instead)"),
    (r"\{\{[A-Z_]+\}\}", "template token left unfilled"),
    (r"http://localhost", "localhost URL hardcoded"),
    (r"127\.0\.0\.1", "localhost IP hardcoded"),
    (r"hover effects on titles and buttons for enhanced", "Figma Make placeholder meta description"),
    (r"\+91 9079273658", "old phone number; should be +91 9468688354"),
    (r"misclifebusiness@gmail\.com\"", "raw email NOT wrapped in mailto link"),
]

# Things that should always be present
REQUIRED_CONTENT = [
    ("Nihal Choudhary", "name in footer"),
    ("misclifebusiness@gmail.com", "email"),
    ("9468688354", "current phone number"),
    ("nihalchoudhary", "linkedin handle"),
    ("wa.me/919468688354", "WhatsApp link"),
]

# Asset path checks: /styles.css and shots/*.png
ASSET_PATTERNS = [
    re.compile(r'href="((?:\.\.\/)*styles\.css)"'),
    re.compile(r'src="(shots/[^"]+)"'),
]

PASS = "[OK]"
FAIL = "[FAIL]"
WARN = "[WARN]"


class Report:
    def __init__(self):
        self.checks = []
        self.failed = 0
        self.warnings = 0

    def ok(self, msg):
        self.checks.append((PASS, msg))

    def fail(self, msg):
        self.checks.append((FAIL, msg))
        self.failed += 1

    def warn(self, msg):
        self.checks.append((WARN, msg))
        self.warnings += 1

    def render(self) -> str:
        out = []
        for status, msg in self.checks:
            out.append(f"  {status}  {msg}")
        out.append("")
        out.append(f"  {self.failed} failure(s), {self.warnings} warning(s)")
        return "\n".join(out)


def validate_files(card_dir: Path, r: Report):
    print(f"\n[1/5] File presence")
    for name in EXPECTED_HTML:
        if (card_dir / name).exists():
            r.ok(f"present: {name}")
        else:
            r.fail(f"missing: {name}")

    if not (ROOT / "styles.css").exists():
        r.fail("missing: ../../styles.css (project-root)")
    else:
        r.ok("present: project-root styles.css")


def validate_content(card_dir: Path, r: Report):
    print(f"\n[2/5] Content patterns (bad)")
    for name in EXPECTED_HTML:
        path = card_dir / name
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for pat, msg in BAD_PATTERNS:
            if re.search(pat, content):
                r.fail(f"{name}: {msg}")

    print(f"\n[3/5] Required content present")
    for needle, label in REQUIRED_CONTENT:
        present_in = []
        for name in EXPECTED_HTML:
            path = card_dir / name
            if not path.exists():
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
            if needle in content:
                present_in.append(name)
        if not present_in:
            r.fail(f"never appears: {label} ({needle!r})")
        else:
            r.ok(f"{label}: appears in {len(present_in)}/{len(EXPECTED_HTML)} pages")


def validate_assets(card_dir: Path, r: Report):
    print(f"\n[4/5] Asset references")
    referenced = set()
    for name in EXPECTED_HTML:
        path = card_dir / name
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for pat in ASSET_PATTERNS:
            for m in pat.finditer(content):
                ref = m.group(1)
                # Resolve relative to the html file's location
                if ref.startswith("../../"):
                    target = (card_dir / ref).resolve()
                else:
                    target = (card_dir / ref).resolve()
                referenced.add((name, ref, target))

    for source, ref, target in sorted(referenced):
        if target.exists():
            size_kb = target.stat().st_size / 1024
            if size_kb > 2000:
                r.warn(f"{source} -> {ref}: {size_kb:.0f}KB (heavy; consider resize)")
            else:
                r.ok(f"{source} -> {ref}: {size_kb:.0f}KB")
        else:
            r.fail(f"{source} -> {ref}: file not found ({target})")


def validate_metadata(card_dir: Path, r: Report):
    print(f"\n[5/5] Page metadata")
    for name in EXPECTED_HTML:
        path = card_dir / name
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"<title>([^<]+)</title>", content)
        if not m:
            r.fail(f"{name}: no <title>")
        elif "Cielo" in m.group(1) and card_dir.name != "cielo":
            r.fail(f"{name}: title still references Cielo: {m.group(1)!r}")
        else:
            r.ok(f"{name}: title looks ok ({m.group(1)[:60]!r})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    args = ap.parse_args()

    card_dir = ROOT / "cards" / args.slug
    if not card_dir.exists():
        sys.exit(f"error: cards/{args.slug}/ not found")

    print(f"Validating cards/{args.slug}/")

    r = Report()
    validate_files(card_dir, r)
    validate_content(card_dir, r)
    validate_assets(card_dir, r)
    validate_metadata(card_dir, r)

    print()
    print(r.render())

    if r.failed == 0:
        print("\nReady to ship.")
        sys.exit(0)
    else:
        print(f"\n{r.failed} failure(s) - fix before shipping.")
        sys.exit(1)


if __name__ == "__main__":
    main()
