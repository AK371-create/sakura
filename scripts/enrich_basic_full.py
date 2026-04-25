#!/usr/bin/env python3
"""Replace basic.hitting and basic.pitching with real API data.

For active MLB players: latest available season (2026 → 2025 → 2024).
For FORMER: career totals.
"""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"

HIT_MAP = {
    "avg": "avg", "h": "hits", "hr": "homeRuns", "rbi": "rbi",
    "sb": "stolenBases", "obp": "obp", "slg": "slg", "ops": "ops",
}
PIT_MAP = {
    "w": "wins", "l": "losses", "era": "era", "so": "strikeOuts",
    "ip": "inningsPitched", "whip": "whip", "sv": "saves", "hld": "holds",
}


def fetch_stats(pid: int, group: str, scope: str, season: int | None = None) -> dict:
    """scope: 'career' or 'season'."""
    if scope == "career":
        url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=career&group={group}&sportId=1"
    else:
        url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=season&group={group}&season={season}&sportId=1"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid} {group} {scope}: {e}")
        return {}
    splits = (data.get("stats") or [{}])[0].get("splits") if data.get("stats") else None
    if not splits:
        return {}
    return splits[0].get("stat") or {}


def map_stat(api_stat: dict, mapping: dict) -> dict:
    out = {}
    for our_key, api_key in mapping.items():
        v = api_stat.get(api_key)
        if v is None or v == "":
            continue
        if our_key in ("h", "hr", "rbi", "sb", "w", "l", "so", "sv", "hld"):
            try:
                out[our_key] = int(v)
            except (TypeError, ValueError):
                pass
        else:
            out[our_key] = str(v)
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
        is_former = data.get("level") == "FORMER"

        had_hitting = data.get("basic", {}).get("hitting") is not None
        had_pitching = data.get("basic", {}).get("pitching") is not None
        ptype = data.get("type")
        # Determine groups to fetch
        groups = []
        if ptype == "two_way" or had_hitting:
            groups.append("hitting")
        if ptype in ("two_way", "pitcher") or had_pitching:
            groups.append("pitching")
        if not groups:
            continue

        new_basic = {}
        season_used: dict[str, int | str] = {}
        for group in groups:
            mapping = HIT_MAP if group == "hitting" else PIT_MAP
            stat = {}
            used_season: int | str | None = None
            if is_former:
                stat = fetch_stats(pid, group, "career")
                used_season = "career"
            else:
                for season in (2026, 2025, 2024):
                    stat = fetch_stats(pid, group, "season", season)
                    time.sleep(0.1)
                    if stat:
                        used_season = season
                        break
            time.sleep(0.1)
            mapped = map_stat(stat, mapping)
            if mapped:
                key_in_basic = "hitting" if group == "hitting" else "pitching"
                new_basic[key_in_basic] = mapped
                if used_season is not None:
                    season_used[key_in_basic] = used_season

        if not new_basic:
            continue
        data["basic"] = new_basic
        if season_used:
            data["basic_season"] = season_used
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        updated += 1
        parts = [f"{g}({len(new_basic[g])} fields, {season_used.get(g, '?')})" for g in new_basic]
        print(f"  {key}: {' + '.join(parts)}")
    print(f"Updated {updated} players' basic stats")


if __name__ == "__main__":
    main()
