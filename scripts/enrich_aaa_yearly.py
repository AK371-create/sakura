#!/usr/bin/env python3
"""AAA選手 (saito, ogasawara) のMILB yearByYearを取得して既存yearlyに反映。
sportId=11 (Triple-A) を含めるため、MLB-only filter を緩和。"""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"

# AAA-only players to enrich
AAA_PLAYERS = ["ogasawara", "saito"]

PIT_MAP = {
    "w": "wins", "l": "losses", "era": "era", "so": "strikeOuts",
    "ip": "inningsPitched", "whip": "whip", "sv": "saves", "hld": "holds",
}


def parse_ip(ip_str):
    try: return float(ip_str)
    except (TypeError, ValueError): return 0.0


def fetch_yearly(pid: int, group: str) -> list[dict]:
    """Fetch all splits regardless of MLB/MILB."""
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=yearByYear&group={group}&hydrate=team"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid}: {e}")
        return []
    splits = []
    for stat_block in data.get("stats", []):
        for s in stat_block.get("splits", []):
            splits.append(s)
    return splits


def aggregate_year(splits, group):
    """Per year, prefer AAA total over individual stints; pick by largest IP."""
    by_year = {}
    teams_by_year = {}
    for s in splits:
        sport_abbr = (s.get("sport") or {}).get("abbreviation", "")
        # Accept MLB and AAA only
        if sport_abbr not in ("MLB", "AAA", ""):
            continue
        try: year = int(s["season"])
        except (KeyError, ValueError): continue
        stat = s.get("stat") or {}
        metric = parse_ip(stat.get("inningsPitched"))
        cur = by_year.get(year)
        if cur is None or metric > cur["_metric"]:
            by_year[year] = {"stat": stat, "_metric": metric, "level": sport_abbr}
        team_abbr = (s.get("team") or {}).get("abbreviation")
        if team_abbr:
            teams_by_year.setdefault(year, [])
            if team_abbr not in teams_by_year[year]:
                teams_by_year[year].append(team_abbr)
    out = {}
    for year, entry in by_year.items():
        teams = teams_by_year.get(year, [])
        team_str = "/".join(teams[:3]) if teams else "?"
        if entry["level"] == "AAA":
            team_str = f"{team_str} (3A)"
        out[year] = {"stat": entry["stat"], "team": team_str, "level": entry["level"]}
    return out


def map_stat(api_stat: dict) -> dict:
    out = {}
    for our_key, api_key in PIT_MAP.items():
        v = api_stat.get(api_key)
        if v is None: continue
        try:
            if our_key in ("w", "l", "so", "sv", "hld"):
                out[our_key] = int(v)
            else:
                out[our_key] = str(v)
        except (TypeError, ValueError): pass
    return out


def main():
    ids = json.loads(IDS_FILE.read_text())
    for key in AAA_PLAYERS:
        pid = ids.get(key)
        if not pid:
            print(f"  {key}: no MLB ID — skipping")
            continue
        f = PLAYERS_DIR / f"{key}.json"
        if not f.exists():
            print(f"  {key}.json not found")
            continue
        data = json.loads(f.read_text())
        splits = fetch_yearly(pid, "pitching")
        time.sleep(0.2)
        agg = aggregate_year(splits, "pitching")
        new_yearly = []
        for year, entry in sorted(agg.items()):
            row = {"year": year, "team": entry["team"], "type": "pit"}
            row.update(map_stat(entry["stat"]))
            if row.get("ip") and parse_ip(row["ip"]) > 0:
                new_yearly.append(row)
        if not new_yearly:
            print(f"  {key}: no AAA/MLB data found")
            continue
        data["yearly"] = new_yearly
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        print(f"  {key}: {len(new_yearly)} rows from API")


if __name__ == "__main__":
    main()
