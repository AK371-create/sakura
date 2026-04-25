#!/usr/bin/env python3
import json, urllib.request

# Try career splits
for stat_type in ["careerStatSplits", "career"]:
    print(f"=== {stat_type} ===")
    url = f"https://statsapi.mlb.com/api/v1/people/660271/stats?stats={stat_type}&group=hitting&sitCodes=vl,vr&sportId=1"
    try:
        d = json.loads(urllib.request.urlopen(url).read())
    except Exception as e:
        print(f"  ERR {e}")
        continue
    for s in d.get("stats", []):
        for sp in s.get("splits", []):
            sit = sp.get("split", {}).get("description")
            stat = sp.get("stat", {})
            print(f"  {sit}: avg={stat.get('avg')} ab={stat.get('atBats')} hr={stat.get('homeRuns')} h={stat.get('hits')}")
