#!/usr/bin/env python3
import json, urllib.request

print("=== Imanaga (684007) pitching 2024 vs LHB/RHB ===")
url = "https://statsapi.mlb.com/api/v1/people/684007/stats?stats=statSplits&group=pitching&sitCodes=vl,vr&season=2024&sportId=1"
d = json.loads(urllib.request.urlopen(url).read())
for s in d.get("stats", []):
    for sp in s.get("splits", []):
        sit = sp.get("split", {}).get("description")
        stat = sp.get("stat", {})
        print(f"  {sit}: avg={stat.get('avg')} ops={stat.get('ops')} hr={stat.get('homeRuns')} k={stat.get('strikeOuts')} bb={stat.get('baseOnBalls')} ab={stat.get('atBats')}")

print("\n=== Ohtani (660271) hitting 2024 vs LHP/RHP ===")
url = "https://statsapi.mlb.com/api/v1/people/660271/stats?stats=statSplits&group=hitting&sitCodes=vl,vr&season=2024&sportId=1"
d = json.loads(urllib.request.urlopen(url).read())
for s in d.get("stats", []):
    for sp in s.get("splits", []):
        sit = sp.get("split", {}).get("description")
        stat = sp.get("stat", {})
        print(f"  {sit}: avg={stat.get('avg')} ops={stat.get('ops')} hr={stat.get('homeRuns')} ab={stat.get('atBats')}")
