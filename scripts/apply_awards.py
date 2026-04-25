#!/usr/bin/env python3
"""Apply awards (filtered to majors) to player JSONs."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
AWARDS_FILE = Path(__file__).parent / "cache" / "awards_resolved.json"


def main():
    awards = json.loads(AWARDS_FILE.read_text())
    updated = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        key = data.get("key")
        if key not in awards:
            continue
        player_awards = awards[key]
        if player_awards:
            data["awards"] = player_awards
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            updated += 1
            print(f"  {key}: {len(player_awards)} awards")
        elif "awards" in data:
            del data["awards"]
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Updated {updated} players")


if __name__ == "__main__":
    main()
