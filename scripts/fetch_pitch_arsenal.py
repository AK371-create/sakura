#!/usr/bin/env python3
"""Fetch real pitch arsenal data from MLB Stats API for each pitcher.

Endpoint: GET /api/v1/people/{id}/stats?stats=pitchArsenal&group=pitching&season=YYYY
Returns: usage % and average speed per pitch type. (BAA/whiff/hard-hit are not in this API.)
"""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "arsenal"
CACHE.mkdir(parents=True, exist_ok=True)

# Pitchers (and two-way) we care about
PITCHERS = [
    "ohtani", "yamamoto", "imanaga", "darvish", "senga", "sasaki",
    "kikuchi", "maeda", "matsui-yuki",
]
# Try seasons in this order (most recent first)
SEASONS = [2026, 2025, 2024]


def fetch(pid: int, season: int) -> list[dict]:
    cache_file = CACHE / f"{pid}_{season}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=pitchArsenal&group=pitching&season={season}"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid} {season}: {e}")
        cache_file.write_text("[]")
        return []
    splits = []
    for stat_block in data.get("stats", []):
        for sp in stat_block.get("splits", []):
            stat = sp.get("stat", {})
            t = stat.get("type", {})
            splits.append({
                "code": t.get("code"),
                "name": t.get("description"),
                "usage": round(float(stat.get("percentage", 0)) * 100, 1),
                "speed": round(float(stat.get("averageSpeed", 0)), 1),
                "count": stat.get("count"),
                "totalPitches": stat.get("totalPitches"),
            })
    cache_file.write_text(json.dumps(splits, ensure_ascii=False, indent=2))
    return splits


def main():
    ids = json.loads(IDS_FILE.read_text())
    out: dict[str, dict] = {}
    for key in PITCHERS:
        pid = ids.get(key)
        if not pid:
            print(f"  {key}: no MLB ID")
            continue
        # Try seasons in order, use first non-empty
        for season in SEASONS:
            splits = fetch(pid, season)
            time.sleep(0.15)
            if splits:
                out[key] = {"season": season, "arsenal": splits}
                print(f"  {key} ({pid}) -> {season}: {len(splits)} pitches")
                break
        else:
            print(f"  {key} ({pid}): no arsenal data found")
    out_file = Path(__file__).parent / "cache" / "arsenal_resolved.json"
    out_file.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
