#!/usr/bin/env python3
"""Apply led/top10 marks to each player's yearly rows based on cached MLB leaderboards.

Reads:
  - src/content/players/*.json
  - scripts/cache/leaders/{year}_{group}_{stat}.json
  - scripts/cache/player_ids.json
Writes back into player JSONs (modifies yearly rows in-place).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
LEADERS_DIR = Path(__file__).parent / "cache" / "leaders"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"

HIT_KEYS = ["avg", "h", "hr", "rbi", "sb", "ops"]
PIT_KEYS = ["era", "w", "so", "ip", "whip"]


def load_leaders(year: int, group: str, key: str) -> list[dict]:
    f = LEADERS_DIR / f"{year}_{group}_{key}.json"
    if not f.exists():
        return []
    try:
        return json.loads(f.read_text())
    except Exception:
        return []


def evaluate(player_id: int, year: int, group: str, key: str) -> str | None:
    """Return 'led' if player led MLB or their league this stat-year, 'top10' if top10 MLB, else None."""
    rows = load_leaders(year, group, key)
    if not rows:
        return None

    # Find player in cache
    me = None
    for r in rows:
        if r.get("id") == player_id:
            me = r
            break
    if me is None:
        return None

    my_rank = me.get("rank")

    # MLB rank 1 → led
    if my_rank == 1:
        return "led"

    # League-leader: highest-ranked AL or NL entry
    al_first = next((r for r in rows if r.get("league") == "AL"), None)
    nl_first = next((r for r in rows if r.get("league") == "NL"), None)
    if al_first and al_first.get("id") == player_id:
        return "led"
    if nl_first and nl_first.get("id") == player_id:
        return "led"

    # Top 10 in MLB
    if my_rank is not None and my_rank <= 10:
        return "top10"
    return None


def process_player(file: Path, ids: dict[str, int]) -> int:
    """Process one player JSON, return count of led+top10 marks added."""
    data = json.loads(file.read_text())
    key = data.get("key")
    pid = ids.get(key)
    if pid is None:
        return 0
    yearly = data.get("yearly") or []
    if not yearly:
        return 0

    marks_added = 0
    for row in yearly:
        year = int(row["year"])
        is_hit = row.get("type") == "hit"
        keys = HIT_KEYS if is_hit else PIT_KEYS
        group = "hitting" if is_hit else "pitching"

        led_list: list[str] = []
        top10_list: list[str] = []
        for k in keys:
            verdict = evaluate(pid, year, group, k)
            if verdict == "led":
                led_list.append(k)
            elif verdict == "top10":
                top10_list.append(k)

        # Replace existing marks (computed from real data is authoritative)
        if led_list:
            row["led"] = led_list
            marks_added += len(led_list)
        elif "led" in row:
            del row["led"]
        if top10_list:
            row["top10"] = top10_list
            marks_added += len(top10_list)
        elif "top10" in row:
            del row["top10"]

    file.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    return marks_added


def main():
    ids = json.loads(IDS_FILE.read_text())
    total = 0
    for f in sorted(PLAYERS_DIR.glob("*.json")):
        added = process_player(f, ids)
        if added:
            print(f"  {f.stem}: {added} marks")
        total += added
    print(f"Total marks applied: {total}")


if __name__ == "__main__":
    main()
