#!/usr/bin/env python3
"""Enrich basic.hitting (career or current season) with OBP/SLG/AVG/OPS from MLB Stats API."""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"


def fetch_career(pid: int) -> dict:
    """Career hitting totals."""
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=career&group=hitting&sportId=1"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR career {pid}: {e}")
        return {}
    splits = data.get("stats", [{}])[0].get("splits", []) if data.get("stats") else []
    if not splits:
        return {}
    return splits[0].get("stat", {})


def fetch_season(pid: int, year: int) -> dict:
    """Single-season hitting totals (MLB only)."""
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=season&group=hitting&season={year}&sportId=1"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR season {pid} {year}: {e}")
        return {}
    splits = data.get("stats", [{}])[0].get("splits", []) if data.get("stats") else []
    if not splits:
        return {}
    return splits[0].get("stat", {})


def fmt_pct(v) -> str:
    if v is None or v == "":
        return ""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    s = f"{f:.3f}"
    if s.startswith("0."):
        s = s[1:]
    return s


def main():
    ids = json.loads(IDS_FILE.read_text())
    updated = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        key = data.get("key")
        pid = ids.get(key)
        if not pid:
            continue
        if not data.get("basic", {}).get("hitting"):
            continue
        is_former = data.get("level") == "FORMER"
        if is_former:
            stat = fetch_career(pid)
            label = "career"
        else:
            # try most recent season with data; fall back through 2026/2025/2024
            stat = {}
            for yr in (2026, 2025, 2024):
                stat = fetch_season(pid, yr)
                if stat:
                    label = f"season {yr}"
                    break
            else:
                continue
        time.sleep(0.15)
        if not stat:
            continue
        h = data["basic"]["hitting"]
        # Always update slg + obp + ops from API
        if stat.get("slg") is not None:
            h["slg"] = fmt_pct(stat["slg"])
        if stat.get("obp") is not None:
            h["obp"] = fmt_pct(stat["obp"])
        if stat.get("ops") is not None:
            h["ops"] = fmt_pct(stat["ops"])
        # Save
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        print(f"  {key}: updated ({label}, SLG={h.get('slg')})")
        updated += 1
    print(f"Updated {updated} batters' basic stats")


if __name__ == "__main__":
    main()
