"""
sample_layout.py — Pixel-sample a screenshot to find element y-positions.

Used to set the `top:` percentage on .shot-mark annotations in audit.html.
The audit screenshots use percentage-based positioning so they survive
any page width — but the percentages must reflect the IMAGE's actual
coordinates, not the rendered frame.

Usage:
    python sample_layout.py <path-to-screenshot.png>
    python sample_layout.py ../cards/cielo/shots/cielo-home.png

Outputs:
    1. Bright-pixel-density rows (UI elements with white text/buttons)
    2. Saved horizontal strips into shots/_strip_<y1>_<y2>.png so you can
       visually identify each region
"""

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Install Pillow first:  pip install Pillow")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: sample_layout.py <path-to-screenshot>")
    img_path = Path(sys.argv[1]).resolve()
    if not img_path.exists():
        sys.exit(f"not found: {img_path}")

    img = Image.open(img_path).convert("RGB")
    W, H = img.size
    print(f"image: {img_path.name}  size: {W}x{H}\n")

    # Step 1 — scan all rows for bright (text/button/pill) density
    print("Bright-pixel rows (groups of 5px steps · cluster threshold > 10):")
    print("-" * 60)

    text_rows = []
    for y in range(0, H, 5):
        pixels = [img.getpixel((x, y)) for x in range(0, W, 4)]
        white = sum(1 for p in pixels if p[0] > 220 and p[1] > 220 and p[2] > 220)
        if white > 10:
            text_rows.append((y, white))

    # Cluster contiguous rows
    clusters = []
    current = []
    prev_y = -100
    for y, w in text_rows:
        if y - prev_y > 25:
            if current:
                clusters.append(current)
            current = []
        current.append((y, w))
        prev_y = y
    if current:
        clusters.append(current)

    # Step 2 — for each cluster, save a horizontal strip and report
    strips_dir = img_path.parent / "_strips"
    strips_dir.mkdir(exist_ok=True)
    for i, cluster in enumerate(clusters):
        y_min = max(0, cluster[0][0] - 12)
        y_max = min(H, cluster[-1][0] + 12)
        strip = img.crop((0, y_min, W, y_max))
        strip.thumbnail((600, 200))
        strip_path = strips_dir / f"_strip_{y_min:03d}_{y_max:03d}.png"
        strip.save(strip_path)
        print(
            f"  cluster {i+1}: y={y_min}-{y_max}  "
            f"({y_min/H*100:5.1f}% - {y_max/H*100:5.1f}%)  "
            f"→ {strip_path.name}"
        )

    print()
    print(
        "Open each strip image to identify which UI element it is, then use\n"
        "the y-percentage range to set the `top:` and `height:` of the\n"
        "corresponding .shot-mark in audit.html."
    )
    print()
    print("Example:")
    print('  <div class="shot-mark" style="left: 30%; top: 27%; width: 40%; height: 18%;"></div>')


if __name__ == "__main__":
    main()
