#!/usr/bin/env python3
"""Enrich pitcher yearly rows with real SV (saves) and HLD (holds) from MLB Stats API."""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "yearly_pit"
CACHE.mkdir(parents=True, exist_ok=True)


def fetch_yearly(pid: int) -> dict[int, dict]:
    """Returns {year: {sv: int, hld: int}} aggregated across teams for MLB only."""
    cache_file = CACHE / f"{pid}.json"
    if cache_file.exists():
        try:
            return {int(k): v for k, v in json.loads(cache_file.read_text()).items()}
        except Exception:
            pass
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=yearByYear&group=pitching"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid}: {e}")
        cache_file.write_text("{}")
        return {}
    by_year: dict[int, dict] = {}
    for stat_block in data.get("stats", []):
        for split in stat_block.get("splits", []):
            league = (split.get("league") or {}).get("name", "")
            sport = (split.get("sport") or {})
            sport_abbr = sport.get("abbreviation", "")
            # MLB only filter: sport.abbreviation == "MLB" or league name contains "League" (AL/NL)
            if sport_abbr and sport_abbr != "MLB":
                continue
            if not (league == "American League" or league == "National League" or league == "AL" or league == "NL"):
                # When league info is missing but sport is MLB, still accept
                if not sport_abbr:
                    continue
            try:
                year = int(split["season"])
            except (KeyError, ValueError):
                continue
            stat = split.get("stat", {})
            sv = int(stat.get("saves") or 0)
            hld = int(stat.get("holds") or 0)
            # Take MAX across splits per year (handles mid-season trades where API returns per-stint + total rows)
            cur = by_year.setdefault(year, {"sv": 0, "hld": 0})
            cur["sv"] = max(cur["sv"], sv)
            cur["hld"] = max(cur["hld"], hld)
    cache_file.write_text(json.dumps({str(k): v for k, v in by_year.items()}))
    return by_year


def main():
    ids = json.loads(IDS_FILE.read_text())
    enriched = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        key = data.get("key")
        pid = ids.get(key)
        if not pid:
            continue
        yearly = data.get("yearly") or []
        if not any(y.get("type") == "pit" for y in yearly):
            continue
        by_year = fetch_yearly(pid)
        time.sleep(0.15)
        if not by_year:
            continue
        changed = False
        for y in yearly:
            if y.get("type") != "pit":
                continue
            year = int(y["year"])
            agg = by_year.get(year)
            if not agg:
                continue
            if agg["sv"] > 0:
                y["sv"] = agg["sv"]
                changed = True
            if agg["hld"] > 0:
                y["hld"] = agg["hld"]
                changed = True
        if changed:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            print(f"  {key}: enriched")
            enriched += 1
    print(f"Enriched {enriched} pitchers' yearly rows")


if __name__ == "__main__":
    main()
