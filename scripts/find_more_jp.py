#!/usr/bin/env python3
"""Search MLB Stats API for additional Japanese MLB alumni."""
import json
import urllib.request
import urllib.parse

CANDIDATES = [
    ("mac-suzuki",       "Mac Suzuki"),
    ("tazawa",           "Junichi Tazawa"),
    ("sawamura",         "Eijun Sawamura"),
    ("ohka",             "Tomokazu Ohka"),
    ("johjima",          "Kenji Johjima"),
    ("igawa",            "Kei Igawa"),
    ("kawasaki",         "Munenori Kawasaki"),
    ("taguchi",          "So Taguchi"),
    ("takahashi-h",      "Hisanori Takahashi"),
    ("otsuka",           "Akinori Otsuka"),
    ("fujikawa",         "Kyuji Fujikawa"),
    ("nishioka",         "Tsuyoshi Nishioka"),
    ("igarashi",         "Ryota Igarashi"),
    ("takatsu",          "Shingo Takatsu"),
    ("kawakami",         "Kenshin Kawakami"),
    ("makita",           "Kazuhisa Makita"),
    ("tadano",           "Kazuhito Tadano"),
    ("kida",             "Masao Kida"),
    ("yabu",             "Keiichi Yabu"),
    ("fukumori",         "Kazuo Fukumori"),
    ("iriki",            "Yusaku Iriki"),
]

found = {}
for key, name in CANDIDATES:
    encoded = urllib.parse.quote(name)
    url = f"https://statsapi.mlb.com/api/v1/people/search?names={encoded}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            d = json.loads(r.read())
    except Exception as e:
        print(f"  {name}: ERR {e}")
        continue
    people = d.get("people", [])
    if not people:
        print(f"  {name}: NOT FOUND")
        continue
    # filter by Japanese birth country
    jp = [p for p in people if p.get("birthCountry") == "Japan"]
    if jp:
        p = jp[0]
        found[key] = (p.get("id"), p.get("fullName"), p.get("primaryPosition", {}).get("abbreviation"))
        print(f"  {key:18s} {p.get('id')} {p.get('fullName')} ({p.get('primaryPosition', {}).get('abbreviation')})")
    else:
        # show first match anyway for debugging
        p = people[0]
        print(f"  {name}: top match not JP — {p.get('fullName')} ({p.get('birthCountry')})")

print(f"\nFound {len(found)} new Japanese players")
print(json.dumps(found, ensure_ascii=False, indent=2))
