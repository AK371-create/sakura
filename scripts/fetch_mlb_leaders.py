#!/usr/bin/env python3
"""Fetch MLB Stats API season leaderboards and cache locally.

Source: statsapi.mlb.com (official MLB Stats API, free, no auth, no ToS issues)
Endpoint: GET /api/v1/stats/leaders
"""
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

CACHE = Path(__file__).parent / "cache" / "leaders"
CACHE.mkdir(parents=True, exist_ok=True)

# Stats to track (MLB Stats API leaderCategories)
HIT_STATS = {
    "avg":  "battingAverage",
    "h":    "hits",
    "hr":   "homeRuns",
    "rbi":  "runsBattedIn",
    "sb":   "stolenBases",
    "obp":  "onBasePercentage",
    "slg":  "sluggingPercentage",
    "ops":  "ops",
}
PIT_STATS = {
    "era":  "earnedRunAverage",
    "w":    "wins",
    "so":   "strikeouts",
    "ip":   "inningsPitched",
    "whip": "walksAndHitsPerInningPitched",
}

YEARS = list(range(1995, 2027))   # 1995-2026 inclusive

LIMIT = 30   # top 30 per board (we want top 10, buffer for ties)
SLEEP = 0.15  # polite delay


def fetch(year: int, group: str, mlb_stat: str, key: str) -> list[dict]:
    """Fetch top N MLB leaders. Returns list of {id, rank, value, league} in MLB-wide rank order."""
    cache_file = CACHE / f"{year}_{group}_{key}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass  # fall through to refetch

    url = (
        f"https://statsapi.mlb.com/api/v1/stats/leaders"
        f"?leaderCategories={mlb_stat}&season={year}&statGroup={group}"
        f"&limit={LIMIT}&sportId=1"
    )
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  WARN: {year} {group}/{key} -> {e}")
        cache_file.write_text("[]")
        return []

    rows: list[dict] = []
    for board in data.get("leagueLeaders", []):
        for entry in board.get("leaders", []):
            person = entry.get("person") or {}
            league = entry.get("league") or {}
            pid = person.get("id")
            if pid is None:
                continue
            rows.append({
                "id": int(pid),
                "rank": entry.get("rank"),
                "value": entry.get("value"),
                "league": league.get("name"),  # "AL" or "NL"
            })
    cache_file.write_text(json.dumps(rows))
    return rows


def main():
    total = 0
    print(f"Fetching MLB leaders for {len(YEARS)} years...")
    for year in YEARS:
        for key, mlb_stat in HIT_STATS.items():
            fetch(year, "hitting", mlb_stat, key)
            total += 1
            time.sleep(SLEEP)
        for key, mlb_stat in PIT_STATS.items():
            fetch(year, "pitching", mlb_stat, key)
            total += 1
            time.sleep(SLEEP)
        print(f"  {year} done ({total} fetched)")
    print(f"Done. {total} leaderboards cached at {CACHE}")


if __name__ == "__main__":
    main()
