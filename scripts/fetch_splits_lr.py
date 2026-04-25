#!/usr/bin/env python3
"""Fetch vs L / vs R splits for each player and apply to their JSON."""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "splits_lr"
CACHE.mkdir(parents=True, exist_ok=True)


def fetch(pid: int, group: str, season: int | str) -> dict:
    """Returns {'vs_left': stat, 'vs_right': stat} or {}."""
    cache_file = CACHE / f"{pid}_{group}_{season}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass
    if season == "career":
        url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=careerStatSplits&group={group}&sitCodes=vl,vr&sportId=1"
    else:
        url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=statSplits&group={group}&sitCodes=vl,vr&season={season}&sportId=1"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            d = json.loads(r.read())
    except Exception as e:
        print(f"    ERR {pid} {group} {season}: {e}")
        cache_file.write_text("{}")
        return {}
    out = {}
    for s in d.get("stats", []):
        for sp in s.get("splits", []):
            desc = (sp.get("split") or {}).get("description", "")
            stat = sp.get("stat", {})
            if "Left" in desc:
                out["vs_left"] = stat
            elif "Right" in desc:
                out["vs_right"] = stat
    cache_file.write_text(json.dumps(out, ensure_ascii=False))
    return out


def fmt_pct(v):
    if v is None: return None
    s = f"{float(v):.3f}"
    return s[1:] if s.startswith("0.") else s


def hit_summary(stat: dict) -> dict:
    return {
        "ab":  stat.get("atBats"),
        "h":   stat.get("hits"),
        "hr":  stat.get("homeRuns"),
        "rbi": stat.get("rbi"),
        "sb":  stat.get("stolenBases"),
        "avg": stat.get("avg"),
        "obp": stat.get("obp"),
        "slg": stat.get("slg"),
        "ops": stat.get("ops"),
    }


def pit_summary(stat: dict) -> dict:
    return {
        "ab":  stat.get("atBats"),
        "ba":  stat.get("avg"),
        "hr":  stat.get("homeRuns"),
        "k":   stat.get("strikeOuts"),
        "bb":  stat.get("baseOnBalls"),
        "ops": stat.get("ops"),
        "obp": stat.get("obp"),
        "slg": stat.get("slg"),
    }


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
        ptype = data.get("type")
        groups = []
        if ptype == "two_way":
            groups = ["hitting", "pitching"]
        elif ptype == "batter":
            groups = ["hitting"]
        elif ptype == "pitcher":
            groups = ["pitching"]
        else:
            continue

        # Determine current-season target
        bs = data.get("basic_season", {})
        season_arg = None
        for g in groups:
            v = bs.get(g)
            if isinstance(v, int):
                season_arg = v
                break

        splits_current = {}
        splits_career = {}
        for g in groups:
            summarize = hit_summary if g == "hitting" else pit_summary

            # Career splits (always for both active and FORMER)
            res_career = fetch(pid, g, "career")
            time.sleep(0.15)
            if res_career:
                packaged = {}
                if "vs_left" in res_career: packaged["vs_left"] = summarize(res_career["vs_left"])
                if "vs_right" in res_career: packaged["vs_right"] = summarize(res_career["vs_right"])
                if packaged: splits_career[g] = packaged

            # Current-season splits (active only)
            if not is_former and season_arg:
                res_cur = fetch(pid, g, season_arg)
                time.sleep(0.15)
                if res_cur:
                    packaged = {}
                    if "vs_left" in res_cur: packaged["vs_left"] = summarize(res_cur["vs_left"])
                    if "vs_right" in res_cur: packaged["vs_right"] = summarize(res_cur["vs_right"])
                    if packaged: splits_current[g] = packaged

        changed = False
        if splits_current:
            data["splits_lr_current"] = splits_current
            if season_arg:
                data["splits_lr_current_season"] = season_arg
            changed = True
        elif "splits_lr_current" in data:
            del data["splits_lr_current"]
            data.pop("splits_lr_current_season", None)
            changed = True
        if splits_career:
            data["splits_lr_career"] = splits_career
            changed = True
        elif "splits_lr_career" in data:
            del data["splits_lr_career"]
            changed = True
        # Remove old single-splits field
        if "splits_lr" in data:
            del data["splits_lr"]
            data.pop("splits_lr_season", None)
            changed = True
        if changed:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            updated += 1
            parts = []
            if splits_current: parts.append(f"current({','.join(splits_current.keys())})")
            if splits_career: parts.append(f"career({','.join(splits_career.keys())})")
            print(f"  {key}: {' + '.join(parts) or '(no splits)'}")

    print(f"Updated {updated} players' L/R splits")


if __name__ == "__main__":
    main()
