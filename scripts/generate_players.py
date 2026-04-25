#!/usr/bin/env python3
"""Generate player JSON files for SakuraBall — MLB + 3A + 過去のMLB."""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "src" / "content" / "players"
OUT.mkdir(parents=True, exist_ok=True)

def H(year, team, avg, h, hr, rbi, sb, ops):
    return {"year": year, "team": team, "type": "hit",
            "avg": avg, "h": h, "hr": hr, "rbi": rbi, "sb": sb, "ops": ops}

def P(year, team, w, l, era, so, ip, whip, sv=None):
    d = {"year": year, "team": team, "type": "pit",
         "w": w, "l": l, "era": era, "so": so, "ip": ip, "whip": whip}
    if sv is not None:
        d["sv"] = sv
    return d

# ========= ACTIVE MLB =========
OHTANI_YEARLY = [
    H(2018, "LAA", ".285", 93, 22, 61, 10, ".925"),
    H(2019, "LAA", ".286", 110, 18, 62, 12, ".848"),
    H(2020, "LAA", ".190", 29, 7, 24, 7, ".657"),
    H(2021, "LAA", ".257", 138, 46, 100, 26, ".965"),
    H(2022, "LAA", ".273", 160, 34, 95, 11, ".875"),
    H(2023, "LAA", ".304", 151, 44, 95, 20, "1.066"),
    H(2024, "LAD", ".310", 197, 54, 130, 59, "1.036"),
    H(2025, "LAD", ".291", 178, 48, 110, 24, ".995"),
    H(2026, "LAD", ".245", 24, 5, 12, 3, ".900"),
    P(2018, "LAA", 4, 2, "3.31", 63, "51.2", "1.16"),
    P(2021, "LAA", 9, 2, "3.18", 156, "130.1", "1.09"),
    P(2022, "LAA", 15, 9, "2.33", 219, "166.0", "1.01"),
    P(2023, "LAA", 10, 5, "3.14", 167, "132.0", "1.06"),
    P(2025, "LAD", 1, 1, "2.87", 32, "31.2", "0.95"),
    P(2026, "LAD", 2, 0, "0.38", 15, "11.2", "0.85"),
]

SUZUKI_YEARLY = [
    H(2022, "CHC", ".262", 104, 14, 46, 9, ".770"),
    H(2023, "CHC", ".285", 146, 20, 74, 6, ".842"),
    H(2024, "CHC", ".283", 138, 21, 73, 16, ".848"),
    H(2025, "CHC", ".278", 152, 25, 85, 12, ".848"),
    H(2026, "CHC", ".276", 28, 4, 11, 1, ".830"),
]

YOSHIDA_YEARLY = [
    H(2023, "BOS", ".289", 153, 15, 72, 8, ".783"),
    H(2024, "BOS", ".280", 109, 10, 56, 2, ".722"),
    H(2025, "BOS", ".275", 132, 12, 60, 1, ".740"),
    H(2026, "BOS", ".291", 30, 2, 8, 0, ".780"),
]

MURAKAMI_YEARLY = [
    H(2026, "CWS", ".253", 22, 10, 19, 0, ".992"),
]

YAMAMOTO_YEARLY = [
    P(2024, "LAD", 7, 2, "3.00", 105, "90.0", "1.11"),
    P(2025, "LAD", 12, 7, "3.10", 180, "170.0", "1.10"),
    P(2026, "LAD", 3, 1, "2.50", 28, "28.2", "1.05"),
]

IMANAGA_YEARLY = [
    P(2024, "CHC", 15, 3, "2.91", 174, "173.1", "1.02"),
    P(2025, "CHC", 13, 7, "3.20", 170, "175.0", "1.10"),
    P(2026, "CHC", 2, 1, "2.15", 22, "25.0", "1.05"),
]

DARVISH_YEARLY = [
    P(2012, "TEX", 16, 9, "3.90", 221, "191.1", "1.28"),
    P(2013, "TEX", 13, 9, "2.83", 277, "209.2", "1.07"),
    P(2014, "TEX", 10, 7, "3.06", 182, "144.1", "1.26"),
    P(2016, "TEX", 7, 5, "3.41", 132, "100.1", "1.16"),
    P(2017, "TEX/LAD", 10, 12, "3.86", 209, "186.2", "1.16"),
    P(2018, "CHC", 1, 3, "4.95", 49, "40.0", "1.43"),
    P(2019, "CHC", 6, 8, "3.98", 229, "178.2", "1.10"),
    P(2020, "CHC", 8, 3, "2.01", 93, "76.0", "0.96"),
    P(2021, "SD", 8, 11, "4.22", 199, "166.1", "1.09"),
    P(2022, "SD", 16, 8, "3.10", 197, "194.2", "0.95"),
    P(2023, "SD", 8, 10, "4.56", 141, "136.1", "1.30"),
    P(2024, "SD", 7, 3, "3.31", 116, "81.2", "1.13"),
    P(2025, "SD", 10, 8, "3.55", 175, "168.0", "1.15"),
    P(2026, "SD", 2, 2, "3.25", 32, "27.2", "1.15"),
]

SENGA_YEARLY = [
    P(2023, "NYM", 12, 7, "2.98", 202, "166.1", "1.22"),
    P(2024, "NYM", 0, 0, "9.00", 9, "5.1", "1.69"),
    P(2025, "NYM", 9, 6, "3.30", 150, "155.0", "1.22"),
    P(2026, "NYM", 2, 1, "2.85", 30, "22.0", "1.15"),
]

SASAKI_YEARLY = [
    P(2025, "LAD", 8, 3, "3.20", 145, "130.0", "1.15"),
    P(2026, "LAD", 2, 0, "2.80", 35, "25.0", "1.00"),
]

KIKUCHI_YEARLY = [
    P(2019, "SEA", 6, 11, "5.46", 116, "161.2", "1.46"),
    P(2020, "SEA", 2, 4, "5.17", 47, "47.0", "1.43"),
    P(2021, "SEA", 7, 9, "4.41", 131, "157.0", "1.38"),
    P(2022, "TOR", 6, 7, "5.19", 124, "100.2", "1.55"),
    P(2023, "TOR", 11, 6, "3.86", 181, "167.2", "1.21"),
    P(2024, "TOR/HOU", 9, 9, "4.05", 206, "175.2", "1.20"),
    P(2025, "LAA", 10, 8, "3.95", 175, "172.0", "1.25"),
    P(2026, "LAA", 2, 1, "3.45", 25, "26.0", "1.20"),
]

MAEDA_YEARLY = [
    P(2016, "LAD", 16, 11, "3.48", 179, "175.2", "1.14"),
    P(2017, "LAD", 13, 6, "4.22", 140, "134.1", "1.16"),
    P(2018, "LAD", 8, 10, "3.81", 153, "125.1", "1.21"),
    P(2019, "LAD", 10, 8, "4.04", 169, "153.2", "1.07"),
    P(2020, "MIN", 6, 1, "2.70", 80, "66.2", "0.75"),
    P(2021, "MIN", 6, 5, "4.66", 113, "106.1", "1.14"),
    P(2023, "MIN", 6, 8, "4.23", 117, "104.1", "1.20"),
    P(2024, "DET", 3, 7, "6.09", 86, "85.2", "1.45"),
    P(2025, "DET", 5, 9, "5.50", 100, "115.0", "1.40"),
    P(2026, "DET", 1, 2, "4.10", 22, "24.0", "1.30"),
]

MATSUI_YUKI_YEARLY = [
    P(2024, "SD", 1, 3, "3.66", 49, "41.2", "1.20", sv=3),
    P(2025, "SD", 2, 2, "3.20", 55, "50.0", "1.18", sv=8),
    P(2026, "SD", 0, 0, "2.50", 12, "10.2", "1.05", sv=5),
]

# ========= AAA =========
SAITO_YEARLY = [
    P(2024, "SAC (3A)", 2, 1, "4.10", 38, "30.0", "1.30"),
    P(2025, "SAC (3A)", 3, 2, "3.50", 42, "35.2", "1.22"),
    P(2026, "SAC (3A)", 1, 0, "3.20", 14, "11.0", "1.20"),
]

OGASAWARA_YEARLY = [
    P(2025, "ROC (3A)", 6, 8, "4.45", 90, "100.0", "1.40"),
    P(2026, "ROC (3A)", 1, 2, "4.20", 18, "20.0", "1.35"),
]

# ========= FORMER (already had data) =========
ICHIRO_YEARLY = [
    H(2001, "SEA", ".350", 242, 8, 69, 56, ".838"),
    H(2002, "SEA", ".321", 208, 8, 51, 31, ".813"),
    H(2003, "SEA", ".312", 212, 13, 62, 34, ".788"),
    H(2004, "SEA", ".372", 262, 8, 60, 36, ".869"),
    H(2005, "SEA", ".303", 206, 15, 68, 33, ".784"),
    H(2006, "SEA", ".322", 224, 9, 49, 45, ".758"),
    H(2007, "SEA", ".351", 238, 6, 68, 37, ".827"),
    H(2008, "SEA", ".310", 213, 6, 42, 43, ".747"),
    H(2009, "SEA", ".352", 225, 11, 46, 26, ".851"),
    H(2010, "SEA", ".315", 214, 6, 43, 42, ".755"),
    H(2011, "SEA", ".272", 184, 5, 47, 40, ".645"),
    H(2012, "SEA/NYY", ".283", 178, 9, 55, 29, ".686"),
    H(2013, "NYY", ".262", 136, 7, 35, 20, ".639"),
    H(2014, "NYY", ".284", 102, 1, 22, 15, ".641"),
    H(2015, "MIA", ".229", 91, 1, 21, 11, ".577"),
    H(2016, "MIA", ".291", 95, 1, 22, 10, ".682"),
    H(2017, "MIA", ".255", 50, 3, 20, 1, ".596"),
    H(2018, "SEA", ".205", 9, 0, 0, 0, ".536"),
]

MATSUI_HIDEKI_YEARLY = [
    H(2003, "NYY", ".287", 179, 16, 106, 2, ".788"),
    H(2004, "NYY", ".298", 174, 31, 108, 3, ".912"),
    H(2005, "NYY", ".305", 192, 23, 116, 2, ".868"),
    H(2006, "NYY", ".302", 53, 8, 29, 0, ".883"),
    H(2007, "NYY", ".285", 156, 25, 103, 0, ".852"),
    H(2008, "NYY", ".294", 99, 9, 45, 0, ".792"),
    H(2009, "NYY", ".274", 117, 28, 90, 0, ".876"),
    H(2010, "LAA", ".274", 132, 21, 84, 0, ".820"),
    H(2011, "OAK", ".251", 117, 12, 72, 0, ".720"),
    H(2012, "TB", ".147", 14, 2, 7, 0, ".459"),
]

NOMO_YEARLY = [
    P(1995, "LAD", 13, 6, "2.54", 236, "191.1", "1.06"),
    P(1996, "LAD", 16, 11, "3.19", 234, "228.1", "1.16"),
    P(1997, "LAD", 14, 12, "4.25", 233, "207.1", "1.39"),
    P(1998, "LAD/NYM", 6, 12, "4.92", 152, "162.2", "1.45"),
    P(1999, "MIL", 12, 8, "4.54", 161, "176.1", "1.47"),
    P(2000, "DET", 8, 12, "4.74", 181, "190.0", "1.39"),
    P(2001, "BOS", 13, 10, "4.50", 220, "198.0", "1.29"),
    P(2002, "LAD", 16, 6, "3.39", 193, "220.1", "1.22"),
    P(2003, "LAD", 16, 13, "3.09", 177, "218.1", "1.21"),
    P(2004, "LAD", 4, 11, "8.25", 54, "84.0", "1.86"),
    P(2005, "TB", 5, 8, "7.24", 59, "100.2", "1.79"),
    P(2008, "KC", 0, 0, "18.69", 18, "8.2", "3.46"),
]

UEHARA_YEARLY = [
    P(2009, "BAL", 2, 4, "4.05", 48, "66.2", "1.05"),
    P(2010, "BAL", 1, 2, "2.86", 55, "44.0", "0.95"),
    P(2011, "BAL/TEX", 2, 4, "1.72", 85, "65.1", "0.71"),
    P(2012, "TEX", 1, 2, "1.75", 43, "36.0", "0.64"),
    P(2013, "BOS", 4, 1, "1.09", 101, "74.1", "0.57", sv=21),
    P(2014, "BOS", 6, 5, "2.52", 80, "64.1", "0.92", sv=26),
    P(2015, "BOS", 2, 3, "2.23", 47, "40.1", "1.04", sv=25),
    P(2016, "BOS", 2, 3, "3.45", 63, "47.0", "0.91", sv=7),
    P(2017, "CHC", 2, 2, "3.98", 40, "43.0", "1.21"),
]

KURODA_YEARLY = [
    P(2008, "LAD", 9, 10, "3.73", 116, "183.1", "1.22"),
    P(2009, "LAD", 8, 7, "3.76", 105, "117.1", "1.16"),
    P(2010, "LAD", 11, 13, "3.39", 159, "196.1", "1.16"),
    P(2011, "LAD", 13, 16, "3.07", 161, "202.0", "1.21"),
    P(2012, "NYY", 16, 11, "3.32", 167, "219.2", "1.17"),
    P(2013, "NYY", 11, 13, "3.31", 150, "201.1", "1.16"),
    P(2014, "NYY", 11, 9, "3.71", 146, "199.0", "1.20"),
]

TANAKA_YEARLY = [
    P(2014, "NYY", 13, 5, "2.77", 141, "136.1", "1.06"),
    P(2015, "NYY", 12, 7, "3.51", 139, "154.0", "0.99"),
    P(2016, "NYY", 14, 4, "3.07", 165, "199.2", "1.08"),
    P(2017, "NYY", 13, 12, "4.74", 194, "178.1", "1.24"),
    P(2018, "NYY", 12, 6, "3.75", 159, "156.0", "1.13"),
    P(2019, "NYY", 11, 9, "4.45", 149, "182.0", "1.24"),
    P(2020, "NYY", 3, 3, "3.56", 44, "48.0", "1.17"),
]

MATSUZAKA_YEARLY = [
    P(2007, "BOS", 15, 12, "4.40", 201, "204.2", "1.32"),
    P(2008, "BOS", 18, 3, "2.90", 154, "167.2", "1.32"),
    P(2009, "BOS", 4, 6, "5.76", 54, "59.1", "1.87"),
    P(2010, "BOS", 9, 6, "4.69", 133, "153.2", "1.37"),
    P(2011, "BOS", 3, 3, "5.30", 47, "37.1", "1.61"),
    P(2012, "BOS", 1, 7, "8.28", 41, "45.2", "1.95"),
    P(2013, "NYM", 3, 3, "4.42", 33, "38.2", "1.42"),
    P(2014, "NYM", 3, 3, "3.89", 57, "83.1", "1.34"),
]

AOKI_YEARLY = [
    H(2012, "MIL", ".288", 150, 10, 50, 30, ".787"),
    H(2013, "MIL", ".286", 171, 8, 37, 20, ".726"),
    H(2014, "KC", ".285", 140, 1, 43, 17, ".704"),
    H(2015, "SF", ".287", 118, 5, 26, 14, ".733"),
    H(2016, "SEA", ".283", 98, 4, 28, 7, ".679"),
    H(2017, "HOU/TOR/NYM", ".272", 97, 7, 28, 5, ".776"),
]

FUKUDOME_YEARLY = [
    H(2008, "CHC", ".257", 127, 10, 58, 12, ".736"),
    H(2009, "CHC", ".259", 138, 11, 54, 6, ".751"),
    H(2010, "CHC", ".263", 108, 13, 44, 7, ".751"),
    H(2011, "CHC/CLE", ".262", 115, 8, 35, 5, ".726"),
    H(2012, "CHW", ".171", 22, 0, 4, 0, ".452"),
]

IWAMURA_YEARLY = [
    H(2007, "TB", ".285", 123, 7, 34, 12, ".755"),
    H(2008, "TB", ".274", 170, 6, 48, 8, ".744"),
    H(2009, "TB", ".290", 68, 1, 22, 0, ".736"),
    H(2010, "PIT/OAK", ".182", 40, 2, 19, 0, ".470"),
]

HIRANO_YEARLY = [
    P(2018, "ARI", 4, 3, "2.44", 59, "75.0", "0.95", sv=3),
    P(2019, "ARI", 5, 5, "4.75", 65, "53.0", "1.45", sv=6),
    P(2020, "SEA", 0, 1, "9.00", 6, "8.0", "2.13", sv=0),
]

TSUTSUGO_YEARLY = [
    H(2020, "TB", ".197", 40, 8, 24, 0, ".708"),
    H(2021, "LAD/PIT", ".220", 53, 8, 29, 0, ".679"),
    H(2022, "PIT/TOR", ".172", 17, 2, 13, 0, ".564"),
]

AKIYAMA_YEARLY = [
    H(2020, "CIN", ".245", 29, 0, 9, 0, ".616"),
    H(2021, "CIN", ".206", 27, 0, 7, 6, ".539"),
]

FUJINAMI_YEARLY = [
    P(2023, "OAK/BAL", 7, 8, "7.18", 96, "79.0", "1.66"),
    P(2024, "NYM", 0, 4, "7.18", 36, "42.2", "1.84"),
]

PLAYERS = [
    {
        "key": "ohtani",
        "name_jp": "大谷翔平", "name_en": "Shohei Ohtani",
        "team_jp": "ロサンゼルス・ドジャース", "team_en": "Los Angeles Dodgers", "team_short": "LAD",
        "league": "NL", "level": "MLB", "type": "two_way",
        "position_jp": "指名打者 / 投手", "position_en": "DH / Pitcher",
        "basic": {
            "hitting": {"avg": ".245", "h": 24, "hr": 5, "rbi": 12, "obp": ".380", "ops": ".900", "sb": 3},
            "pitching": {"era": "0.38", "w": 2, "l": 0, "so": 15, "whip": "0.85", "ip": "11.2"},
        },
        "savant": {
            "hitting": {
                "exit_velocity_avg": 94.1, "launch_angle_avg": 12.6,
                "barrel_batted_rate": 22.1, "hard_hit_percent": 51.5,
                "xba": ".261", "xslg": ".516", "xwoba": ".388",
                "k_percent": 24.1, "bb_percent": 13.8,
            },
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 44.4, "ba": ".105", "whiff": 27.0, "hard_hit": 40.7},
                {"pitch": "SL", "jp": "スイーパー", "en": "Sweeper", "usage": 28.2, "ba": ".150", "whiff": 38.5, "hard_hit": 30.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 14.6, "ba": ".080", "whiff": 50.0, "hard_hit": 22.0},
                {"pitch": "FC", "jp": "カッター", "en": "Cutter", "usage": 8.4, "ba": ".180", "whiff": 22.0, "hard_hit": 35.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 4.4, "ba": ".200", "whiff": 28.0, "hard_hit": 33.0},
            ],
        },
        "yearly": OHTANI_YEARLY,
    },
    {
        "key": "suzuki",
        "name_jp": "鈴木誠也", "name_en": "Seiya Suzuki",
        "team_jp": "シカゴ・カブス", "team_en": "Chicago Cubs", "team_short": "CHC",
        "league": "NL", "level": "MLB", "type": "batter",
        "position_jp": "右翼手", "position_en": "Right Fielder",
        "basic": {"hitting": {"avg": ".276", "h": 28, "hr": 4, "rbi": 11, "obp": ".355", "ops": ".830", "sb": 1}},
        "savant": {
            "hitting": {
                "exit_velocity_avg": 90.5, "launch_angle_avg": 13.2,
                "barrel_batted_rate": 11.8, "hard_hit_percent": 47.3,
                "xba": ".270", "xslg": ".470", "xwoba": ".355",
                "k_percent": 22.1, "bb_percent": 9.2,
            },
        },
        "yearly": SUZUKI_YEARLY,
    },
    {
        "key": "yoshida",
        "name_jp": "吉田正尚", "name_en": "Masataka Yoshida",
        "team_jp": "ボストン・レッドソックス", "team_en": "Boston Red Sox", "team_short": "BOS",
        "league": "AL", "level": "MLB", "type": "batter",
        "position_jp": "左翼手 / 指名打者", "position_en": "LF / DH",
        "basic": {"hitting": {"avg": ".291", "h": 30, "hr": 2, "rbi": 8, "obp": ".345", "ops": ".780", "sb": 0}},
        "savant": {
            "hitting": {
                "exit_velocity_avg": 88.2, "launch_angle_avg": 11.5,
                "barrel_batted_rate": 7.2, "hard_hit_percent": 40.5,
                "xba": ".285", "xslg": ".430", "xwoba": ".342",
                "k_percent": 11.5, "bb_percent": 7.8,
            },
        },
        "yearly": YOSHIDA_YEARLY,
    },
    {
        "key": "murakami",
        "name_jp": "村上宗隆", "name_en": "Munetaka Murakami",
        "team_jp": "シカゴ・ホワイトソックス", "team_en": "Chicago White Sox", "team_short": "CWS",
        "league": "AL", "level": "MLB", "type": "batter",
        "position_jp": "三塁手", "position_en": "Third Baseman",
        "basic": {"hitting": {"avg": ".253", "h": 22, "hr": 10, "rbi": 19, "obp": ".420", "ops": ".992", "sb": 0}},
        "savant": {
            "hitting": {
                "exit_velocity_avg": 96.0, "launch_angle_avg": 16.5,
                "barrel_batted_rate": 24.5, "hard_hit_percent": 64.2,
                "xba": ".255", "xslg": ".649", "xwoba": ".433",
                "k_percent": 32.1, "bb_percent": 19.3,
            },
        },
        "yearly": MURAKAMI_YEARLY,
    },
    {
        "key": "yamamoto",
        "name_jp": "山本由伸", "name_en": "Yoshinobu Yamamoto",
        "team_jp": "ロサンゼルス・ドジャース", "team_en": "Los Angeles Dodgers", "team_short": "LAD",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "2.50", "w": 3, "l": 1, "so": 28, "whip": "1.05", "ip": "28.2"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 38.2, "ba": ".210", "whiff": 23.5, "hard_hit": 38.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 24.4, "ba": ".145", "whiff": 45.2, "hard_hit": 25.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 18.6, "ba": ".165", "whiff": 38.0, "hard_hit": 28.0},
                {"pitch": "FC", "jp": "カッター", "en": "Cutter", "usage": 11.5, "ba": ".220", "whiff": 21.0, "hard_hit": 36.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 7.3, "ba": ".180", "whiff": 36.0, "hard_hit": 30.0},
            ],
        },
        "yearly": YAMAMOTO_YEARLY,
    },
    {
        "key": "imanaga",
        "name_jp": "今永昇太", "name_en": "Shota Imanaga",
        "team_jp": "シカゴ・カブス", "team_en": "Chicago Cubs", "team_short": "CHC",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "2.15", "w": 2, "l": 1, "so": 22, "whip": "1.05", "ip": "25.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 44.5, "ba": ".163", "whiff": 17.7, "hard_hit": 63.3},
                {"pitch": "FS", "jp": "スプリット", "en": "Split-Finger", "usage": 33.4, "ba": ".175", "whiff": 41.9, "hard_hit": 20.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 14.2, "ba": ".210", "whiff": 32.0, "hard_hit": 35.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 7.9, "ba": ".185", "whiff": 28.0, "hard_hit": 25.0},
            ],
        },
        "yearly": IMANAGA_YEARLY,
    },
    {
        "key": "darvish",
        "name_jp": "ダルビッシュ有", "name_en": "Yu Darvish",
        "team_jp": "サンディエゴ・パドレス", "team_en": "San Diego Padres", "team_short": "SD",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "3.25", "w": 2, "l": 2, "so": 32, "whip": "1.15", "ip": "27.2"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FC", "jp": "カッター", "en": "Cutter", "usage": 22.3, "ba": ".225", "whiff": 26.0, "hard_hit": 37.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 20.8, "ba": ".180", "whiff": 36.5, "hard_hit": 28.0},
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 18.2, "ba": ".240", "whiff": 21.0, "hard_hit": 41.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 14.5, "ba": ".165", "whiff": 42.0, "hard_hit": 22.0},
                {"pitch": "SI", "jp": "シンカー", "en": "Sinker", "usage": 12.0, "ba": ".265", "whiff": 12.0, "hard_hit": 45.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 12.2, "ba": ".200", "whiff": 30.0, "hard_hit": 30.0},
            ],
        },
        "yearly": DARVISH_YEARLY,
    },
    {
        "key": "senga",
        "name_jp": "千賀滉大", "name_en": "Kodai Senga",
        "team_jp": "ニューヨーク・メッツ", "team_en": "New York Mets", "team_short": "NYM",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "2.85", "w": 2, "l": 1, "so": 30, "whip": "1.15", "ip": "22.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 38.5, "ba": ".220", "whiff": 24.0, "hard_hit": 40.0},
                {"pitch": "FS", "jp": "お化けフォーク", "en": "Ghost Forkball", "usage": 28.4, "ba": ".145", "whiff": 48.5, "hard_hit": 18.0},
                {"pitch": "FC", "jp": "カッター", "en": "Cutter", "usage": 18.2, "ba": ".210", "whiff": 23.0, "hard_hit": 35.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 10.5, "ba": ".195", "whiff": 32.0, "hard_hit": 30.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 4.4, "ba": ".180", "whiff": 35.0, "hard_hit": 25.0},
            ],
        },
        "yearly": SENGA_YEARLY,
    },
    {
        "key": "sasaki",
        "name_jp": "佐々木朗希", "name_en": "Roki Sasaki",
        "team_jp": "ロサンゼルス・ドジャース", "team_en": "Los Angeles Dodgers", "team_short": "LAD",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "2.80", "w": 2, "l": 0, "so": 35, "whip": "1.00", "ip": "25.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 48.5, "ba": ".180", "whiff": 28.0, "hard_hit": 35.0},
                {"pitch": "FS", "jp": "フォーク", "en": "Forkball", "usage": 36.2, "ba": ".120", "whiff": 52.0, "hard_hit": 20.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 15.3, "ba": ".195", "whiff": 35.0, "hard_hit": 28.0},
            ],
        },
        "yearly": SASAKI_YEARLY,
    },
    {
        "key": "kikuchi",
        "name_jp": "菊池雄星", "name_en": "Yusei Kikuchi",
        "team_jp": "ロサンゼルス・エンゼルス", "team_en": "Los Angeles Angels", "team_short": "LAA",
        "league": "AL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "3.45", "w": 2, "l": 1, "so": 25, "whip": "1.20", "ip": "26.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 38.4, "ba": ".235", "whiff": 22.0, "hard_hit": 42.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 28.6, "ba": ".185", "whiff": 38.0, "hard_hit": 28.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 18.5, "ba": ".210", "whiff": 28.0, "hard_hit": 32.0},
                {"pitch": "CH", "jp": "チェンジアップ", "en": "Changeup", "usage": 14.5, "ba": ".200", "whiff": 35.0, "hard_hit": 30.0},
            ],
        },
        "yearly": KIKUCHI_YEARLY,
    },
    {
        "key": "maeda",
        "name_jp": "前田健太", "name_en": "Kenta Maeda",
        "team_jp": "デトロイト・タイガース", "team_en": "Detroit Tigers", "team_short": "DET",
        "league": "AL", "level": "MLB", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "4.10", "w": 1, "l": 2, "so": 22, "whip": "1.30", "ip": "24.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 38.2, "ba": ".200", "whiff": 36.0, "hard_hit": 30.0},
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 30.5, "ba": ".265", "whiff": 18.0, "hard_hit": 45.0},
                {"pitch": "CH", "jp": "チェンジアップ", "en": "Changeup", "usage": 18.4, "ba": ".220", "whiff": 30.0, "hard_hit": 35.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 12.9, "ba": ".180", "whiff": 38.0, "hard_hit": 28.0},
            ],
        },
        "yearly": MAEDA_YEARLY,
    },
    {
        "key": "matsui-yuki",
        "name_jp": "松井裕樹", "name_en": "Yuki Matsui",
        "team_jp": "サンディエゴ・パドレス", "team_en": "San Diego Padres", "team_short": "SD",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "basic": {"pitching": {"era": "2.50", "w": 0, "l": 0, "sv": 5, "so": 12, "whip": "1.05", "ip": "10.2"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 42.5, "ba": ".165", "whiff": 42.0, "hard_hit": 25.0},
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 35.2, "ba": ".200", "whiff": 25.0, "hard_hit": 38.0},
                {"pitch": "CH", "jp": "チェンジアップ", "en": "Changeup", "usage": 22.3, "ba": ".180", "whiff": 38.0, "hard_hit": 28.0},
            ],
        },
        "yearly": MATSUI_YUKI_YEARLY,
    },
    # AAA
    {
        "key": "saito",
        "name_jp": "齋藤友貴哉", "name_en": "Yukiya Saito",
        "team_jp": "サクラメント・リバーキャッツ (3A)", "team_en": "Sacramento River Cats (AAA)", "team_short": "SAC",
        "league": "AAA", "level": "AAA", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "basic": {"pitching": {"era": "3.20", "w": 1, "l": 0, "so": 14, "whip": "1.20", "ip": "11.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 58.0, "ba": ".250", "whiff": 22.0, "hard_hit": 38.0},
                {"pitch": "FS", "jp": "フォーク", "en": "Forkball", "usage": 28.0, "ba": ".180", "whiff": 38.0, "hard_hit": 28.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 14.0, "ba": ".220", "whiff": 30.0, "hard_hit": 32.0},
            ],
        },
        "yearly": SAITO_YEARLY,
    },
    {
        "key": "ogasawara",
        "name_jp": "小笠原慎之介", "name_en": "Shinnosuke Ogasawara",
        "team_jp": "ロチェスター・レッドウィングス (3A)", "team_en": "Rochester Red Wings (AAA)", "team_short": "ROC",
        "league": "AAA", "level": "AAA", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "4.20", "w": 1, "l": 2, "so": 18, "whip": "1.35", "ip": "20.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 40.0, "ba": ".275", "whiff": 16.0, "hard_hit": 44.0},
                {"pitch": "CH", "jp": "チェンジアップ", "en": "Changeup", "usage": 25.0, "ba": ".220", "whiff": 30.0, "hard_hit": 32.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 20.0, "ba": ".240", "whiff": 26.0, "hard_hit": 35.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 15.0, "ba": ".200", "whiff": 28.0, "hard_hit": 30.0},
            ],
        },
        "yearly": OGASAWARA_YEARLY,
    },
    # FORMER
    {
        "key": "ichiro",
        "name_jp": "イチロー", "name_en": "Ichiro Suzuki",
        "team_jp": "シアトル・マリナーズ", "team_en": "Seattle Mariners", "team_short": "SEA",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2001-2019",
        "current_status_jp": "2019年引退", "current_status_en": "Retired (2019)",
        "basic": {"hitting": {"avg": ".311", "h": 3089, "hr": 117, "rbi": 780, "obp": ".355", "ops": ".757", "sb": 509}},
        "yearly": ICHIRO_YEARLY,
    },
    {
        "key": "matsui-hideki",
        "name_jp": "松井秀喜", "name_en": "Hideki Matsui",
        "team_jp": "ニューヨーク・ヤンキース", "team_en": "New York Yankees", "team_short": "NYY",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手 / 指名打者", "position_en": "OF / DH",
        "mlb_years": "2003-2012",
        "current_status_jp": "2012年引退", "current_status_en": "Retired (2012)",
        "basic": {"hitting": {"avg": ".282", "h": 1253, "hr": 175, "rbi": 760, "obp": ".360", "ops": ".822", "sb": 7}},
        "yearly": MATSUI_HIDEKI_YEARLY,
    },
    {
        "key": "nomo",
        "name_jp": "野茂英雄", "name_en": "Hideo Nomo",
        "team_jp": "ロサンゼルス・ドジャース", "team_en": "Los Angeles Dodgers", "team_short": "LAD",
        "league": "NL", "level": "FORMER", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "mlb_years": "1995-2008",
        "current_status_jp": "2008年引退", "current_status_en": "Retired (2008)",
        "basic": {"pitching": {"era": "4.24", "w": 123, "l": 109, "so": 1918, "whip": "1.35", "ip": "1976.1"}},
        "yearly": NOMO_YEARLY,
    },
    {
        "key": "uehara",
        "name_jp": "上原浩治", "name_en": "Koji Uehara",
        "team_jp": "ボストン・レッドソックス", "team_en": "Boston Red Sox", "team_short": "BOS",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2009-2017",
        "current_status_jp": "2019年引退", "current_status_en": "Retired (2019)",
        "basic": {"pitching": {"era": "2.66", "w": 22, "l": 26, "sv": 95, "so": 562, "whip": "0.89", "ip": "440.2"}},
        "yearly": UEHARA_YEARLY,
    },
    {
        "key": "kuroda",
        "name_jp": "黒田博樹", "name_en": "Hiroki Kuroda",
        "team_jp": "ニューヨーク・ヤンキース", "team_en": "New York Yankees", "team_short": "NYY",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "mlb_years": "2008-2014",
        "current_status_jp": "2016年引退(NPB復帰後)", "current_status_en": "Retired (2016)",
        "basic": {"pitching": {"era": "3.45", "w": 79, "l": 79, "so": 986, "whip": "1.18", "ip": "1319.0"}},
        "yearly": KURODA_YEARLY,
    },
    {
        "key": "tanaka",
        "name_jp": "田中将大", "name_en": "Masahiro Tanaka",
        "team_jp": "ニューヨーク・ヤンキース", "team_en": "New York Yankees", "team_short": "NYY",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "mlb_years": "2014-2020",
        "current_status_jp": "東北楽天イーグルス所属", "current_status_en": "Now with Rakuten (NPB)",
        "basic": {"pitching": {"era": "3.74", "w": 78, "l": 46, "so": 991, "whip": "1.13", "ip": "1054.1"}},
        "yearly": TANAKA_YEARLY,
    },
    {
        "key": "matsuzaka",
        "name_jp": "松坂大輔", "name_en": "Daisuke Matsuzaka",
        "team_jp": "ボストン・レッドソックス", "team_en": "Boston Red Sox", "team_short": "BOS",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "mlb_years": "2007-2014",
        "current_status_jp": "2021年引退", "current_status_en": "Retired (2021)",
        "basic": {"pitching": {"era": "4.45", "w": 56, "l": 43, "so": 720, "whip": "1.41", "ip": "790.2"}},
        "yearly": MATSUZAKA_YEARLY,
    },
    {
        "key": "aoki",
        "name_jp": "青木宣親", "name_en": "Norichika Aoki",
        "team_jp": "ミルウォーキー・ブルワーズ", "team_en": "Milwaukee Brewers", "team_short": "MIL",
        "league": "NL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2012-2017",
        "current_status_jp": "2024年引退", "current_status_en": "Retired (2024)",
        "basic": {"hitting": {"avg": ".285", "h": 774, "hr": 35, "rbi": 192, "obp": ".350", "ops": ".743", "sb": 79}},
        "yearly": AOKI_YEARLY,
    },
    {
        "key": "fukudome",
        "name_jp": "福留孝介", "name_en": "Kosuke Fukudome",
        "team_jp": "シカゴ・カブス", "team_en": "Chicago Cubs", "team_short": "CHC",
        "league": "NL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2008-2012",
        "current_status_jp": "2022年引退", "current_status_en": "Retired (2022)",
        "basic": {"hitting": {"avg": ".258", "h": 510, "hr": 42, "rbi": 195, "obp": ".359", "ops": ".739", "sb": 13}},
        "yearly": FUKUDOME_YEARLY,
    },
    {
        "key": "iwamura",
        "name_jp": "岩村明憲", "name_en": "Akinori Iwamura",
        "team_jp": "タンパベイ・レイズ", "team_en": "Tampa Bay Rays", "team_short": "TB",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "二塁手 / 三塁手", "position_en": "2B / 3B",
        "mlb_years": "2007-2010",
        "current_status_jp": "2017年引退", "current_status_en": "Retired (2017)",
        "basic": {"hitting": {"avg": ".267", "h": 415, "hr": 16, "rbi": 145, "obp": ".346", "ops": ".710", "sb": 21}},
        "yearly": IWAMURA_YEARLY,
    },
    {
        "key": "hirano",
        "name_jp": "平野佳寿", "name_en": "Yoshihisa Hirano",
        "team_jp": "アリゾナ・ダイヤモンドバックス", "team_en": "Arizona Diamondbacks", "team_short": "ARI",
        "league": "NL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2018-2020",
        "current_status_jp": "オリックス・バファローズ所属", "current_status_en": "Now with Orix (NPB)",
        "basic": {"pitching": {"era": "4.40", "w": 6, "l": 7, "sv": 9, "so": 130, "whip": "1.32", "ip": "133.0"}},
        "yearly": HIRANO_YEARLY,
    },
    {
        "key": "tsutsugo",
        "name_jp": "筒香嘉智", "name_en": "Yoshitomo Tsutsugo",
        "team_jp": "タンパベイ・レイズ", "team_en": "Tampa Bay Rays", "team_short": "TB",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手 / 一塁手", "position_en": "OF / 1B",
        "mlb_years": "2020-2022",
        "current_status_jp": "横浜DeNAベイスターズ所属", "current_status_en": "Now with Yokohama DeNA (NPB)",
        "basic": {"hitting": {"avg": ".211", "h": 110, "hr": 14, "rbi": 53, "obp": ".311", "ops": ".677", "sb": 0}},
        "yearly": TSUTSUGO_YEARLY,
    },
    {
        "key": "akiyama",
        "name_jp": "秋山翔吾", "name_en": "Shogo Akiyama",
        "team_jp": "シンシナティ・レッズ", "team_en": "Cincinnati Reds", "team_short": "CIN",
        "league": "NL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2020-2021",
        "current_status_jp": "広島東洋カープ所属", "current_status_en": "Now with Hiroshima (NPB)",
        "basic": {"hitting": {"avg": ".224", "h": 56, "hr": 0, "rbi": 16, "obp": ".300", "ops": ".574", "sb": 6}},
        "yearly": AKIYAMA_YEARLY,
    },
    {
        "key": "fujinami",
        "name_jp": "藤浪晋太郎", "name_en": "Shintaro Fujinami",
        "team_jp": "オークランド・アスレチックス", "team_en": "Oakland Athletics", "team_short": "OAK",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2023-2024",
        "current_status_jp": "NPB復帰", "current_status_en": "Returned to NPB",
        "basic": {"pitching": {"era": "7.18", "w": 7, "l": 12, "so": 132, "whip": "1.66", "ip": "121.2"}},
        "yearly": FUJINAMI_YEARLY,
    },
]

UPDATED = "2026-04-25"
for p in PLAYERS:
    p.setdefault("updated_at", UPDATED)
    path = OUT / f"{p['key']}.json"
    path.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")

mlb = sum(1 for p in PLAYERS if p["level"] == "MLB")
aaa = sum(1 for p in PLAYERS if p["level"] == "AAA")
former = sum(1 for p in PLAYERS if p["level"] == "FORMER")
with_yearly = sum(1 for p in PLAYERS if p.get("yearly"))
print(f"Generated {len(PLAYERS)} players: MLB={mlb} AAA={aaa} FORMER={former}")
print(f"With yearly data: {with_yearly}/{len(PLAYERS)}")
