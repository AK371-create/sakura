#!/usr/bin/env python3
"""記事内の数値・選手名と現状JSONとの整合性を検査。
mock値が残っていそうな記事をフラグ付け。"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
ART = ROOT / "src" / "content" / "articles"
PLR = ROOT / "src" / "content" / "players"

# Load player data
players = {}
for f in PLR.glob("*.json"):
    p = json.loads(f.read_text(encoding="utf-8"))
    players[p["key"]] = p
    players[p["name_jp"]] = p
    players[p["name_en"]] = p

# Mock-like statcast values that I generated and aren't real
SUSPECT_STATCAST = ["Barrel率 22.1", "Hard-Hit率 51.5", "94.1mph", "94.1 mph", "xwOBA .388", ".388",
                    "barrel_batted_rate", "exit_velocity_avg"]

# Players that no longer exist in our roster (Murakami removed)
REMOVED = ["村上宗隆", "村上"]

# Players whose mock 2026 numbers appear in articles but are no longer accurate
MOCK_2026 = {
    "大谷5本塁打": "ohtani",      # I made up "5 HR by April"
    "5本塁打到達": "ohtani",
    ".245": "ohtani",
    "今永": "imanaga",            # 2.15 ERA mock
    "ERA 2.15": "imanaga",
    "OPS .992": "murakami",       # Murakami removed
    "村上宗隆": "murakami",
}


def scan_article(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    body = " ".join(d.get("body_jp", []))
    summary = d.get("summary_jp", "")
    text = body + " " + summary

    flags = []

    # 1. Removed players referenced
    for name in REMOVED:
        if name in text:
            flags.append(("REMOVED", f"削除済み選手 '{name}' を参照"))

    # 2. Suspicious statcast numbers
    for s in SUSPECT_STATCAST:
        if s in text:
            flags.append(("MOCK_STATCAST", f"私が生成した擬似Statcast値: {s}"))
            break  # one is enough per article

    # 3. Mock 2026 stat references
    for term, player_key in MOCK_2026.items():
        if term in text and player_key not in REMOVED:
            flags.append(("MOCK_2026", f"私が生成した2026年序盤数値: {term}"))
            break

    return flags, d


def main():
    rows = []
    total = 0
    for f in sorted(ART.glob("*.json")):
        total += 1
        flags, d = scan_article(f)
        if flags:
            rows.append((d["slug"], d["title_jp"], flags))

    print(f"## 記事ファクトチェック\n対象: {total}記事 / 問題あり: {len(rows)}記事\n")
    for slug, title, flags in rows:
        print(f"### {title}")
        print(f"  slug: {slug}")
        for kind, detail in flags:
            print(f"    🔴 [{kind}] {detail}")
        print()


if __name__ == "__main__":
    main()
