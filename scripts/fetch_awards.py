#!/usr/bin/env python3
"""Fetch awards for each player from MLB Stats API and apply to player JSONs."""
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"
CACHE = Path(__file__).parent / "cache" / "awards"
CACHE.mkdir(parents=True, exist_ok=True)


# Major awards we care about. Each entry: (regex matching `name`, normalized JP label, category)
# Order matters: more specific patterns first.
MAJOR_AWARDS = [
    # Top tier
    (r"World Series MVP",                      "ワールドシリーズMVP",   "ws-mvp"),
    (r"\b(AL|NL) MVP\b",                       "リーグMVP",             "mvp"),
    (r"(AL|NL) Cy Young",                      "サイ・ヤング賞",        "cy"),
    (r"Jackie Robinson (AL|NL) Rookie of the Year",  "新人王",          "roy"),
    (r"^(AL|NL) Rookie of the Year$",          "新人王",                "roy"),
    # High tier
    (r"\bALCS MVP\b",                          "ア・リーグCS MVP",      "alcs-mvp"),
    (r"\bNLCS MVP\b",                          "ナ・リーグCS MVP",      "nlcs-mvp"),
    (r"(AL|NL) Silver Slugger",                "シルバースラッガー賞",  "silver"),
    (r"Rawlings (AL|NL) Gold Glove",           "ゴールドグラブ賞",      "gold"),
    (r"Hank Aaron",                            "ハンク・アーロン賞",    "aaron"),
    (r"(AL|NL) Comeback Player of the Year",   "カムバック賞",          "comeback"),
    (r"Commissioner.s Historic",               "コミッショナー特別賞",  "historic"),
    # All-Star (count)
    (r"\b(AL|NL) All-Star\b",                  "オールスター",          "as"),
]
SKIP = [
    r"Player of the Week",
    r"Player of the Month",
    r"Rookie of the Month",
    r"Pitcher of the Week",
    r"Pitcher of the Month",
    r"Mariners MVP", r"Yankees MVP", r"Dodgers MVP", r"Cubs MVP", r"Athletics MVP",
    r"Defensive Player of the Year",
    r"WBC",  # World Baseball Classic — separate
    r"Outstanding Rookie", r"Outstanding Player",
    r"All-MLB",  # noisy duplicates
    r"Top \d+ MLB Player",
    r"Babe Ruth", r"Edgar Martinez",  # specialty awards
]


def fetch_player(pid: int) -> list[dict]:
    cache_file = CACHE / f"{pid}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/awards"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {pid}: {e}")
        cache_file.write_text("[]")
        return []
    awards = data.get("awards", [])
    cache_file.write_text(json.dumps(awards, ensure_ascii=False, indent=2))
    return awards


def classify(name: str) -> tuple[str, str] | None:
    """Return (jp_label, category) for an award name, or None if to skip."""
    if not name:
        return None
    for pat in SKIP:
        if re.search(pat, name, re.I):
            return None
    for pat, jp, cat in MAJOR_AWARDS:
        if re.search(pat, name, re.I):
            return (jp, cat)
    return None


def main():
    ids = json.loads(IDS_FILE.read_text())
    out: dict[str, list] = {}
    for key, pid in ids.items():
        awards = fetch_player(pid)
        time.sleep(0.15)
        major: list[dict] = []
        seen: set[tuple[str, int]] = set()
        for a in awards:
            name = a.get("name", "")
            classified = classify(name)
            if not classified:
                continue
            jp, cat = classified
            try:
                year = int(a.get("season"))
            except (TypeError, ValueError):
                continue
            # dedupe (same award+year sometimes appears twice)
            sig = (cat, year)
            if sig in seen:
                continue
            seen.add(sig)
            major.append({"year": year, "label": jp, "cat": cat, "raw": name})
        major.sort(key=lambda x: (x["year"], x["cat"]))
        out[key] = major
        if major:
            print(f"  {key}: {len(major)} awards (e.g., {major[0]['label']} {major[0]['year']})")
    out_file = Path(__file__).parent / "cache" / "awards_resolved.json"
    out_file.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
