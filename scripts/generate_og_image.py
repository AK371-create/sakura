#!/usr/bin/env python3
"""Generate OG default image (1200x630 PNG)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import urllib.request

OUT = Path(__file__).parent.parent / "public" / "og-default.png"
W, H = 1200, 630

# Background gradient (warm cream)
img = Image.new("RGB", (W, H), (250, 248, 247))
draw = ImageDraw.Draw(img)

# Subtle radial accent (top right)
for r in range(400, 0, -2):
    alpha = int(40 * (r / 400))
    bbox = (W - r, -r, W + r, r * 2)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse(bbox, fill=(214, 37, 56, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

# Try Noto fonts (Linux) or fall back to default
def try_font(*paths, size=20):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

font_eyebrow = try_font(
    "/usr/share/fonts/truetype/inter/Inter-Medium.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    size=28,
)
font_brand = try_font(
    "/usr/share/fonts/truetype/inter/Inter-ExtraBold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    size=92,
)
font_jp = try_font(
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto-cjk/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    size=42,
)
font_url = try_font(
    "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    size=24,
)
font_stat_label = try_font(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    size=18,
)
font_stat_value = try_font(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    size=80,
)

# Sakura mark (left side)
draw.ellipse((100, 100, 220, 220), outline=(214, 37, 56), width=4)
# Two petals
draw.polygon([(160, 105), (140, 145), (160, 160), (180, 145)], fill=(214, 37, 56))
draw.polygon([(160, 215), (140, 175), (160, 160), (180, 175)], fill=(214, 37, 56, 153))

# Eyebrow
draw.text((100, 290), "JAPANESE MLB / 2026 SEASON", font=font_eyebrow, fill=(107, 99, 96))

# Brand
draw.text((100, 350), "SakuraBall", font=font_brand, fill=(26, 22, 20))

# JP tagline
draw.text((100, 460), "日本人MLB、データで読む。", font=font_jp, fill=(26, 22, 20))

# URL
draw.text((100, 540), "sakuraballpark.com", font=font_url, fill=(156, 148, 143))

# Right side stats
right_x = 800
draw.text((right_x, 130), "PLAYERS", font=font_stat_label, fill=(156, 148, 143))
draw.text((right_x, 160), "26", font=font_stat_value, fill=(214, 37, 56))
draw.text((right_x + 200, 130), "ARTICLES", font=font_stat_label, fill=(156, 148, 143))
draw.text((right_x + 200, 160), "40", font=font_stat_value, fill=(26, 22, 20))
draw.text((right_x, 320), "SEASONS", font=font_stat_label, fill=(156, 148, 143))
draw.text((right_x, 350), "1995-26", font=font_stat_value, fill=(26, 22, 20))

img.save(OUT, "PNG", optimize=True)
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
