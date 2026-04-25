#!/usr/bin/env python3
"""Resolve MLB Stats API player IDs for all our players via search endpoint."""
import json
import time
import urllib.request
from pathlib import Path

OUT = Path(__file__).parent / "cache" / "player_ids.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# key -> search name (must match MLB roster)
PLAYERS = {
    "ohtani":       "Shohei Ohtani",
    "suzuki":       "Seiya Suzuki",
    "yoshida":      "Masataka Yoshida",
    "yamamoto":     "Yoshinobu Yamamoto",
    "imanaga":      "Shota Imanaga",
    "darvish":      "Yu Darvish",
    "senga":        "Kodai Senga",
    "sasaki":       "Roki Sasaki",
    "kikuchi":      "Yusei Kikuchi",
    "maeda":        "Kenta Maeda",
    "matsui-yuki":  "Yuki Matsui",
    "saito":        "Yukiya Saito",
    "ogasawara":    "Shinnosuke Ogasawara",
    "ichiro":       "Ichiro Suzuki",
    "matsui-hideki":"Hideki Matsui",
    "nomo":         "Hideo Nomo",
    "uehara":       "Koji Uehara",
    "kuroda":       "Hiroki Kuroda",
    "tanaka":       "Masahiro Tanaka",
    "matsuzaka":    "Daisuke Matsuzaka",
    "aoki":         "Norichika Aoki",
    "fukudome":     "Kosuke Fukudome",
    "iwamura":      "Akinori Iwamura",
    "hirano":       "Yoshihisa Hirano",
    "tsutsugo":     "Yoshi Tsutsugo",
    "akiyama":      "Shogo Akiyama",
    "fujinami":     "Shintaro Fujinami",
    # murakami is not (yet) in MLB
}


def search(name: str) -> int | None:
    url = f"https://statsapi.mlb.com/api/v1/people/search?names={urllib.parse.quote(name)}"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  ERR {name}: {e}")
        return None
    people = data.get("people", [])
    if not people:
        return None
    # Try exact match first
    for p in people:
        if p.get("fullName", "").lower() == name.lower():
            return int(p["id"])
    # Fall back to first match
    return int(people[0]["id"])


def main():
    import urllib.parse
    globals()["urllib"].parse = urllib.parse  # ensure available

    existing = {}
    if OUT.exists():
        existing = json.loads(OUT.read_text())

    out: dict[str, int] = dict(existing)
    for key, name in PLAYERS.items():
        if key in out and out[key]:
            print(f"  {key}: {out[key]} (cached)")
            continue
        pid = search(name)
        if pid:
            out[key] = pid
            print(f"  {key} ({name}) -> {pid}")
        else:
            print(f"  {key} ({name}) -> NOT FOUND")
        time.sleep(0.2)

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
