#!/usr/bin/env python3
"""Replace all manual yearly stats with real MLB Stats API yearByYear data.

For each player + group (hitting/pitching), fetch yearByYear and merge real stats
into the yearly array. Handles mid-season trades by selecting the season-totals split
(highest atBats / innings).
"""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "yearly_full"
CACHE.mkdir(parents=True, exist_ok=True)

# Mapping: our key -> (api_field, formatter)
HIT_MAP = {
    "avg":  ("avg", str),
    "h":    ("hits", int),
    "hr":   ("homeRuns", int),
    "rbi":  ("rbi", int),
    "sb":   ("stolenBases", int),
    "obp":  ("obp", str),
    "slg":  ("slg", str),
    "ops":  ("ops", str),
}
PIT_MAP = {
    "w":    ("wins", int),
    "l":    ("losses", int),
    "era":  ("era", str),
    "so":   ("strikeOuts", int),
    "ip":   ("inningsPitched", str),
    "whip": ("whip", str),
    "sv":   ("saves", int),
    "hld":  ("holds", int),
}


def parse_ip(ip_str):
    try:
        return float(ip_str)
    except (TypeError, ValueError):
        return 0.0


def fetch_year_by_year(pid: int, group: str) -> list[dict]:
    cache_file = CACHE / f"{pid}_{group}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=yearByYear&group={group}&hydrate=team"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid} {group}: {e}")
        cache_file.write_text("[]")
        return []
    splits = []
    for stat_block in data.get("stats", []):
        for s in stat_block.get("splits", []):
            splits.append(s)
    cache_file.write_text(json.dumps(splits, ensure_ascii=False, indent=2))
    return splits


def aggregate_by_year(splits, group):
    """Returns {year: aggregated_split} where aggregated takes the season totals row.

    Strategy: for each year, find split with the largest atBats (hitting) or
    inningsPitched (pitching). That's typically the season totals row when
    multiple stints exist.
    """
    by_year = {}
    teams_by_year = {}
    for s in splits:
        sport_abbr = (s.get("sport") or {}).get("abbreviation", "")
        # MLB only; skip MILB / spring
        if sport_abbr and sport_abbr != "MLB":
            continue
        league = (s.get("league") or {}).get("name", "")
        if not (league in ("American League", "National League") or sport_abbr == "MLB"):
            continue
        try:
            year = int(s["season"])
        except (KeyError, ValueError):
            continue

        stat = s.get("stat") or {}
        if group == "hitting":
            metric = int(stat.get("atBats") or 0)
        else:
            metric = parse_ip(stat.get("inningsPitched"))

        cur = by_year.get(year)
        if cur is None or metric > cur["_metric"]:
            by_year[year] = {"stat": stat, "_metric": metric}

        team_abbr = (s.get("team") or {}).get("abbreviation")
        if team_abbr:
            teams_by_year.setdefault(year, [])
            if team_abbr not in teams_by_year[year]:
                teams_by_year[year].append(team_abbr)

    # Format output
    out = {}
    for year, entry in by_year.items():
        teams = teams_by_year.get(year, [])
        if not teams:
            team_str = "?"
        elif len(teams) == 1:
            team_str = teams[0]
        else:
            team_str = "/".join(teams[:3])
        out[year] = {"stat": entry["stat"], "team": team_str}
    return out


def map_stat(api_stat: dict, mapping: dict) -> dict:
    """Convert API stat dict to our key format."""
    out = {}
    for our_key, (api_key, fmt) in mapping.items():
        v = api_stat.get(api_key)
        if v is None:
            continue
        try:
            if fmt is int:
                out[our_key] = int(v)
            elif fmt is str:
                # Some rate stats may come as strings already; some as floats
                out[our_key] = str(v) if not isinstance(v, str) else v
        except (TypeError, ValueError):
            continue
    return out


def main():
    ids = json.loads(IDS_FILE.read_text())
    updated = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        key = data.get("key")
        pid = ids.get(key)
        if not pid:
            continue

        # Determine which groups apply
        existing_yearly = data.get("yearly") or []
        has_hit = any(y.get("type") == "hit" for y in existing_yearly)
        has_pit = any(y.get("type") == "pit" for y in existing_yearly)
        # Also for two-way, both
        if data.get("type") == "two_way":
            has_hit = has_pit = True
        elif data.get("type") == "batter":
            has_hit = True
        elif data.get("type") == "pitcher":
            has_pit = True

        new_yearly: list[dict] = []

        if has_hit:
            splits = fetch_year_by_year(pid, "hitting")
            time.sleep(0.15)
            agg = aggregate_by_year(splits, "hitting")
            for year, entry in sorted(agg.items()):
                row = {"year": year, "team": entry["team"], "type": "hit"}
                row.update(map_stat(entry["stat"], HIT_MAP))
                # Skip empty rows (rare but possible if all fields missing)
                if "h" in row or "avg" in row:
                    new_yearly.append(row)

        if has_pit:
            splits = fetch_year_by_year(pid, "pitching")
            time.sleep(0.15)
            agg = aggregate_by_year(splits, "pitching")
            for year, entry in sorted(agg.items()):
                row = {"year": year, "team": entry["team"], "type": "pit"}
                row.update(map_stat(entry["stat"], PIT_MAP))
                # Filter rows with no IP (didn't actually pitch)
                if row.get("ip") and parse_ip(row["ip"]) > 0:
                    new_yearly.append(row)

        if not new_yearly:
            continue  # API returned nothing — keep existing manual data

        data["yearly"] = new_yearly
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        updated += 1
        h_count = sum(1 for r in new_yearly if r["type"] == "hit")
        p_count = sum(1 for r in new_yearly if r["type"] == "pit")
        print(f"  {key}: {h_count} hit + {p_count} pit rows from API")

    print(f"Updated {updated} players' yearly arrays from real API data")


if __name__ == "__main__":
    main()
