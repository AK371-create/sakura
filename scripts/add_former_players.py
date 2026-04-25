#!/usr/bin/env python3
"""Add new FORMER MLB Japanese players: search API → generate JSON + register ID."""
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent.parent
PLAYERS_DIR = ROOT / "src" / "content" / "players"
IDS_FILE = Path(__file__).parent / "cache" / "player_ids.json"

# Japanese names mapping for known players (will be needed for name_jp)
JP_NAMES = {
    "mac-suzuki":     ("マック鈴木", "Mac Suzuki"),
    "tazawa":         ("田澤純一", "Junichi Tazawa"),
    "johjima":        ("城島健司", "Kenji Johjima"),
    "igawa":          ("井川慶", "Kei Igawa"),
    "kawasaki":       ("川崎宗則", "Munenori Kawasaki"),
    "taguchi":        ("田口壮", "So Taguchi"),
    "takahashi-h":    ("高橋尚成", "Hisanori Takahashi"),
    "otsuka":         ("大塚晶則", "Akinori Otsuka"),
    "fujikawa":       ("藤川球児", "Kyuji Fujikawa"),
    "nishioka":       ("西岡剛", "Tsuyoshi Nishioka"),
    "igarashi":       ("五十嵐亮太", "Ryota Igarashi"),
    "takatsu":        ("高津臣吾", "Shingo Takatsu"),
    "kawakami":       ("川上憲伸", "Kenshin Kawakami"),
    "makita":         ("牧田和久", "Kazuhisa Makita"),
    "tadano":         ("多田野数人", "Kazuhito Tadano"),
    "kida":           ("木田優夫", "Masao Kida"),
    "yabu":           ("藪恵壹", "Keiichi Yabu"),
    "fukumori":       ("福盛和男", "Kazuo Fukumori"),
    "iriki":          ("入来祐作", "Yusaku Iriki"),
    "ohka":           ("大家友和", "Tomokazu Ohka"),
    "sawamura":       ("澤村拓一", "Hirokazu Sawamura"),
    "okajima":        ("岡島秀樹", "Hideki Okajima"),
    "nakajima-h":     ("中島宏之", "Hiroyuki Nakajima"),
    "tanaka-k":       ("田中賢介", "Kensuke Tanaka"),
    "muranaka":       ("村中恭兵", "Kyohei Muranaka"),  # may not be in MLB
    # ===== Additional candidates =====
    "matsuzaka-r":    ("松坂亘", "Wataru Matsuzaka"),  # may not exist
    "okazaki":        ("岡崎太一", "Taichi Okazaki"),
    "shimazaki":      ("島崎毅", "Tsuyoshi Shimazaki"),
    "yoshii":         ("吉井理人", "Masato Yoshii"),
    "shinjo":         ("新庄剛志", "Tsuyoshi Shinjo"),
    "sasaki-k":       ("佐々木主浩", "Kazuhiro Sasaki"),
    "ishii":          ("石井一久", "Kazuhisa Ishii"),
    "tomonaga":       ("友永翔太", "Shota Tomonaga"),
    "kuroki":         ("黒木知宏", "Tomohiro Kuroki"),
    "wada":           ("和田毅", "Tsuyoshi Wada"),
    "nakamura":       ("中村紀洋", "Norihiro Nakamura"),
    "iwakuma":        ("岩隈久志", "Hisashi Iwakuma"),
    "ohba":           ("大場翔太", "Shota Ohba"),
    "saito-t":        ("斎藤隆", "Takashi Saito"),
    "matsumoto":      ("松本哲也", "Tetsuya Matsumoto"),
}

# Try multiple search patterns since some are unfindable directly
SEARCH_PATTERNS = {
    "ohka":       ["Tomokazu Ohka", "Tomo Ohka", "Ohka"],
    "sawamura":   ["Hirokazu Sawamura", "Eijun Sawamura", "Sawamura"],
    "okajima":    ["Hideki Okajima"],
    "nakajima-h": ["Hiroyuki Nakajima"],
    "tanaka-k":   ["Kensuke Tanaka"],
}

# MLB team abbreviation -> Japanese team name
TEAM_JP = {
    "ARI": "アリゾナ・ダイヤモンドバックス", "ATL": "アトランタ・ブレーブス",
    "BAL": "ボルティモア・オリオールズ", "BOS": "ボストン・レッドソックス",
    "CHC": "シカゴ・カブス", "CHW": "シカゴ・ホワイトソックス", "CWS": "シカゴ・ホワイトソックス",
    "CIN": "シンシナティ・レッズ", "CLE": "クリーブランド・ガーディアンズ",
    "COL": "コロラド・ロッキーズ", "DET": "デトロイト・タイガース",
    "HOU": "ヒューストン・アストロズ", "KC": "カンザスシティ・ロイヤルズ",
    "LAA": "ロサンゼルス・エンゼルス", "LAD": "ロサンゼルス・ドジャース",
    "MIA": "マイアミ・マーリンズ", "MIL": "ミルウォーキー・ブルワーズ",
    "MIN": "ミネソタ・ツインズ", "NYM": "ニューヨーク・メッツ",
    "NYY": "ニューヨーク・ヤンキース", "OAK": "オークランド・アスレチックス",
    "PHI": "フィラデルフィア・フィリーズ", "PIT": "ピッツバーグ・パイレーツ",
    "SD": "サンディエゴ・パドレス", "SEA": "シアトル・マリナーズ",
    "SF": "サンフランシスコ・ジャイアンツ", "STL": "セントルイス・カージナルス",
    "TB": "タンパベイ・レイズ", "TEX": "テキサス・レンジャーズ",
    "TOR": "トロント・ブルージェイズ", "WSH": "ワシントン・ナショナルズ",
}
TEAM_EN = {
    "ARI": "Arizona Diamondbacks", "ATL": "Atlanta Braves",
    "BAL": "Baltimore Orioles", "BOS": "Boston Red Sox",
    "CHC": "Chicago Cubs", "CHW": "Chicago White Sox", "CWS": "Chicago White Sox",
    "CIN": "Cincinnati Reds", "CLE": "Cleveland Guardians",
    "COL": "Colorado Rockies", "DET": "Detroit Tigers",
    "HOU": "Houston Astros", "KC": "Kansas City Royals",
    "LAA": "Los Angeles Angels", "LAD": "Los Angeles Dodgers",
    "MIA": "Miami Marlins", "MIL": "Milwaukee Brewers",
    "MIN": "Minnesota Twins", "NYM": "New York Mets",
    "NYY": "New York Yankees", "OAK": "Oakland Athletics",
    "PHI": "Philadelphia Phillies", "PIT": "Pittsburgh Pirates",
    "SD": "San Diego Padres", "SEA": "Seattle Mariners",
    "SF": "San Francisco Giants", "STL": "St. Louis Cardinals",
    "TB": "Tampa Bay Rays", "TEX": "Texas Rangers",
    "TOR": "Toronto Blue Jays", "WSH": "Washington Nationals",
}


def search_player(patterns):
    for name in patterns:
        encoded = urllib.parse.quote(name)
        url = f"https://statsapi.mlb.com/api/v1/people/search?names={encoded}"
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                d = json.loads(r.read())
        except Exception:
            continue
        people = d.get("people", [])
        jp = [p for p in people if p.get("birthCountry") == "Japan"]
        if jp:
            return jp[0]
        if people:
            # Some may have country missing; try first if name contains expected substring
            for p in people:
                if name.split()[-1].lower() in p.get("fullName", "").lower():
                    return p
    return None


def fetch_career_summary(pid: int, group: str):
    """Get MLB years and last team."""
    url = f"https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=yearByYear&group={group}&hydrate=team"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            d = json.loads(r.read())
    except Exception:
        return None, None
    stats = d.get("stats") or []
    if not stats:
        return None, None
    years = []
    teams = []
    for s in stats[0].get("splits", []):
        sport_abbr = (s.get("sport") or {}).get("abbreviation", "")
        if sport_abbr != "MLB":
            continue
        try:
            y = int(s["season"])
            years.append(y)
            t = (s.get("team") or {}).get("abbreviation")
            if t:
                teams.append((y, t))
        except Exception:
            continue
    if not years:
        return None, None
    mlb_years = f"{min(years)}-{max(years)}" if min(years) != max(years) else f"{min(years)}"
    last_team = teams[-1][1] if teams else None
    return mlb_years, last_team


def main():
    ids = json.loads(IDS_FILE.read_text())
    new_ids = {}
    added_keys = []

    for key, (jp_name, en_name_default) in JP_NAMES.items():
        if key in ids:
            print(f"  {key}: already registered (id={ids[key]}) — skipping")
            continue

        patterns = SEARCH_PATTERNS.get(key, [en_name_default])
        person = search_player(patterns)
        time.sleep(0.2)
        if not person:
            print(f"  {key} ({jp_name}): NOT FOUND")
            continue

        pid = person["id"]
        full_name_en = person.get("fullName", en_name_default)
        position = (person.get("primaryPosition") or {}).get("abbreviation", "P")
        is_pitcher = position == "P"
        ptype = "pitcher" if is_pitcher else "batter"
        position_jp = "投手" if is_pitcher else {
            "C": "捕手", "1B": "一塁手", "2B": "二塁手", "3B": "三塁手",
            "SS": "遊撃手", "LF": "左翼手", "CF": "中堅手", "RF": "右翼手",
            "OF": "外野手", "DH": "指名打者",
        }.get(position, "野手")
        position_en = "Pitcher" if is_pitcher else position

        # Fetch career years + last team
        mlb_years, last_team = fetch_career_summary(pid, "pitching" if is_pitcher else "hitting")
        time.sleep(0.2)
        if not mlb_years:
            print(f"  {key}: no MLB data found in API")
            continue

        team_jp = TEAM_JP.get(last_team, "")
        team_en = TEAM_EN.get(last_team, last_team or "")

        # Construct league guess (we'll set NL by default; correctness depends on team)
        AL_TEAMS = {"BAL", "BOS", "NYY", "TB", "TOR", "CHW", "CWS", "CLE", "DET", "KC", "MIN",
                    "HOU", "LAA", "OAK", "SEA", "TEX"}
        NL_TEAMS = {"ATL", "MIA", "NYM", "PHI", "WSH", "CHC", "CIN", "MIL", "PIT", "STL",
                    "ARI", "COL", "LAD", "SD", "SF"}
        if last_team in AL_TEAMS:
            league = "AL"
        elif last_team in NL_TEAMS:
            league = "NL"
        else:
            league = "AL"

        data = {
            "key": key,
            "name_jp": jp_name,
            "name_en": full_name_en,
            "team_jp": team_jp,
            "team_en": team_en,
            "team_short": last_team or "",
            "league": league,
            "level": "FORMER",
            "type": ptype,
            "position_jp": position_jp,
            "position_en": position_en,
            "mlb_years": mlb_years,
            "current_status_jp": "MLB引退/NPB復帰",
            "current_status_en": "Retired or returned to NPB",
            "basic": {("pitching" if is_pitcher else "hitting"): {}},  # filled by enrich
            "updated_at": "2026-04-25",
        }
        out_file = PLAYERS_DIR / f"{key}.json"
        out_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        new_ids[key] = pid
        added_keys.append((key, pid, full_name_en, mlb_years, last_team))
        print(f"  + {key:14s} id={pid} {full_name_en} ({mlb_years}, last={last_team})")

    if new_ids:
        ids.update(new_ids)
        IDS_FILE.write_text(json.dumps(ids, ensure_ascii=False, indent=2))
        print(f"\nWrote {len(new_ids)} new IDs to {IDS_FILE}")
    print(f"\nAdded {len(added_keys)} players. Run enrich_yearly_full.py + enrich_basic_full.py + apply_marks.py next.")


if __name__ == "__main__":
    main()
