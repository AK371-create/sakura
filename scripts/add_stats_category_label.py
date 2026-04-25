#!/usr/bin/env python3
"""Inject 'stats' category label into category maps across pages."""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
JP_FILES = [
    "src/pages/articles/index.astro",
    "src/pages/articles/[slug].astro",
    "src/pages/index.astro",
]
EN_FILES = [
    "src/pages/en/articles/index.astro",
    "src/pages/en/articles/[slug].astro",
    "src/pages/en/index.astro",
]

for rel in JP_FILES:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    if "stats:" in s and '"用語解説"' in s:
        print(f"  skip (already has stats): {rel}")
        continue
    # Insert after the "market" line
    new = re.sub(
        r'(market: "市場",)',
        r'\1\n  stats: "用語解説",',
        s,
        count=1,
    )
    if new != s:
        p.write_text(new, encoding="utf-8")
        print(f"  updated: {rel}")
    else:
        print(f"  no match: {rel}")

for rel in EN_FILES:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    if 'stats: "STATS"' in s:
        print(f"  skip (already has stats): {rel}")
        continue
    new = re.sub(
        r'(market: "MARKET",)',
        r'\1\n  stats: "STATS",',
        s,
        count=1,
    )
    if new != s:
        p.write_text(new, encoding="utf-8")
        print(f"  updated: {rel}")
    else:
        print(f"  no match: {rel}")
