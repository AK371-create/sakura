#!/usr/bin/env python3
"""Search MLB API for Saito with name variations."""
import json
import urllib.request
import urllib.parse

NAMES = ["Saito", "Yukiya Saito", "Tomoki Saito", "Yuki Saito", "Tomokiya Saito"]
for name in NAMES:
    encoded = urllib.parse.quote(name)
    url = f"https://statsapi.mlb.com/api/v1/people/search?names={encoded}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            d = json.loads(r.read())
    except Exception as e:
        print(f"  {name}: ERR {e}")
        continue
    print(f"\n=== {name} ===")
    for p in d.get("people", [])[:5]:
        country = p.get("birthCountry", "?")
        bd = p.get("birthDate", "?")
        pos = (p.get("primaryPosition") or {}).get("abbreviation", "?")
        print(f"  {p.get('id')} {p.get('fullName')} ({country}, {bd}, {pos})")
