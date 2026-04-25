#!/usr/bin/env python3
"""Enrich batter yearly rows with real OBP / SLG from MLB Stats API."""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "yearly_hit"
CACHE.mkdir(parents=True, exist_ok=True)


def fetch_yearly(pid: int) -> dict[int, dict]:
    """Returns {year: {obp, slg, ops, avg}} (MLB only)."""
    cache_file = CACHE / f"{pid}.json"
    if cache_file.exists():
        try:
            return {int(k): v for k, v in json.loads(cache_file.read_text()).items()}
        except Exception:
            pass
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=yearByYear&group=hitting"
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
            sport = split.get("sport") or {}
            sport_abbr = sport.get("abbreviation", "")
            if sport_abbr and sport_abbr != "MLB":
                continue
            if not (league in ("American League", "National League") or sport_abbr == "MLB"):
                continue
            try:
                year = int(split["season"])
            except (KeyError, ValueError):
                continue
            stat = split.get("stat", {})
            obp = stat.get("obp") or stat.get("onBasePercentage")
            slg = stat.get("slg") or stat.get("sluggingPercentage")
            if obp is None and slg is None:
                continue
            cur = by_year.setdefault(year, {"obp": None, "slg": None})
            # Take best (largest) when multiple splits per year (mid-season trades)
            for k, v in (("obp", obp), ("slg", slg)):
                if v is None:
                    continue
                try:
                    val = float(v)
                except (TypeError, ValueError):
                    continue
                if cur[k] is None or val > cur[k]:
                    cur[k] = val
    cache_file.write_text(json.dumps({str(k): v for k, v in by_year.items()}))
    return by_year


def fmt_pct(v) -> str:
    """Format a fraction like 0.355 as '.355' (MLB convention)."""
    if v is None:
        return ""
    s = f"{v:.3f}"
    if s.startswith("0."):
        s = s[1:]
    return s


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
        if not any(y.get("type") == "hit" for y in yearly):
            continue
        by_year = fetch_yearly(pid)
        time.sleep(0.15)
        if not by_year:
            continue
        changed = False
        for y in yearly:
            if y.get("type") != "hit":
                continue
            year = int(y["year"])
            agg = by_year.get(year)
            if not agg:
                continue
            if agg.get("obp") is not None:
                y["obp"] = fmt_pct(agg["obp"])
                changed = True
            if agg.get("slg") is not None:
                y["slg"] = fmt_pct(agg["slg"])
                changed = True
        if changed:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            print(f"  {key}: enriched")
            enriched += 1
    print(f"Enriched {enriched} batters' yearly rows")


if __name__ == "__main__":
    main()
