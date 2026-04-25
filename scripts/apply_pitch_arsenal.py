#!/usr/bin/env python3
"""Replace mock pitch_arsenal data in player JSONs with real MLB Stats API data."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
ARSENAL_FILE = Path(__file__).parent / "cache" / "arsenal_resolved.json"

# MLB Stats API pitch code -> JP / EN labels
PITCH_LABELS = {
    "FF": ("4シーム", "4-Seam Fastball"),
    "FT": ("ツーシーム", "2-Seam Fastball"),
    "FC": ("カッター", "Cutter"),
    "FS": ("スプリット", "Splitter"),
    "FA": ("ファストボール", "Fastball"),
    "SI": ("シンカー", "Sinker"),
    "SL": ("スライダー", "Slider"),
    "ST": ("スイーパー", "Sweeper"),
    "SV": ("スラーブ", "Slurve"),
    "CU": ("カーブ", "Curveball"),
    "CS": ("スローカーブ", "Slow Curve"),
    "KC": ("ナックルカーブ", "Knuckle-Curve"),
    "CH": ("チェンジアップ", "Changeup"),
    "EP": ("イーファス", "Eephus"),
    "KN": ("ナックルボール", "Knuckleball"),
    "FO": ("フォーク", "Forkball"),
    "SC": ("スクリューボール", "Screwball"),
}


def main():
    arsenal = json.loads(ARSENAL_FILE.read_text())
    updated = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        key = data.get("key")
        if key not in arsenal:
            continue
        info = arsenal[key]
        season = info["season"]
        splits = info["arsenal"]

        # Convert to display format, sort by usage desc, drop tiny (<1%) usage
        pitches = []
        for s in splits:
            code = s.get("code") or "?"
            usage = s.get("usage", 0)
            if usage < 1.0:  # ignore one-off pitches
                continue
            jp, en = PITCH_LABELS.get(code, (code, code))
            pitches.append({
                "pitch": code,
                "jp": jp,
                "en": en,
                "usage": usage,
                "speed": s.get("speed"),
            })
        pitches.sort(key=lambda p: -p["usage"])

        if "savant" not in data:
            data["savant"] = {}
        data["savant"]["pitch_arsenal"] = pitches
        data["savant"]["arsenal_season"] = season
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        print(f"  {key}: {len(pitches)} pitches (season {season})")
        updated += 1
    print(f"Updated {updated} players")


if __name__ == "__main__":
    main()
