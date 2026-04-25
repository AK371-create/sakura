#!/usr/bin/env python3
"""Generate player JSON files for SakuraBall — MLB + 3A + 過去のMLB."""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "src" / "content" / "players"
OUT.mkdir(parents=True, exist_ok=True)

# Year-by-year stats for select notable players
# Format hitting: [year, team, avg, h, hr, rbi, sb, ops]
# Format pitching: [year, team, w, l, era, so, ip, whip]

ICHIRO_YEARLY = [
    {"year": 2001, "team": "SEA", "type": "hit", "avg": ".350", "h": 242, "hr": 8, "rbi": 69, "sb": 56, "ops": ".838"},
    {"year": 2002, "team": "SEA", "type": "hit", "avg": ".321", "h": 208, "hr": 8, "rbi": 51, "sb": 31, "ops": ".813"},
    {"year": 2003, "team": "SEA", "type": "hit", "avg": ".312", "h": 212, "hr": 13, "rbi": 62, "sb": 34, "ops": ".788"},
    {"year": 2004, "team": "SEA", "type": "hit", "avg": ".372", "h": 262, "hr": 8, "rbi": 60, "sb": 36, "ops": ".869"},
    {"year": 2005, "team": "SEA", "type": "hit", "avg": ".303", "h": 206, "hr": 15, "rbi": 68, "sb": 33, "ops": ".784"},
    {"year": 2006, "team": "SEA", "type": "hit", "avg": ".322", "h": 224, "hr": 9, "rbi": 49, "sb": 45, "ops": ".758"},
    {"year": 2007, "team": "SEA", "type": "hit", "avg": ".351", "h": 238, "hr": 6, "rbi": 68, "sb": 37, "ops": ".827"},
    {"year": 2008, "team": "SEA", "type": "hit", "avg": ".310", "h": 213, "hr": 6, "rbi": 42, "sb": 43, "ops": ".747"},
    {"year": 2009, "team": "SEA", "type": "hit", "avg": ".352", "h": 225, "hr": 11, "rbi": 46, "sb": 26, "ops": ".851"},
    {"year": 2010, "team": "SEA", "type": "hit", "avg": ".315", "h": 214, "hr": 6, "rbi": 43, "sb": 42, "ops": ".755"},
    {"year": 2011, "team": "SEA", "type": "hit", "avg": ".272", "h": 184, "hr": 5, "rbi": 47, "sb": 40, "ops": ".645"},
    {"year": 2012, "team": "SEA/NYY", "type": "hit", "avg": ".283", "h": 178, "hr": 9, "rbi": 55, "sb": 29, "ops": ".686"},
    {"year": 2013, "team": "NYY", "type": "hit", "avg": ".262", "h": 136, "hr": 7, "rbi": 35, "sb": 20, "ops": ".639"},
    {"year": 2014, "team": "NYY", "type": "hit", "avg": ".284", "h": 102, "hr": 1, "rbi": 22, "sb": 15, "ops": ".641"},
    {"year": 2015, "team": "MIA", "type": "hit", "avg": ".229", "h": 91, "hr": 1, "rbi": 21, "sb": 11, "ops": ".577"},
    {"year": 2016, "team": "MIA", "type": "hit", "avg": ".291", "h": 95, "hr": 1, "rbi": 22, "sb": 10, "ops": ".682"},
    {"year": 2017, "team": "MIA", "type": "hit", "avg": ".255", "h": 50, "hr": 3, "rbi": 20, "sb": 1, "ops": ".596"},
    {"year": 2018, "team": "SEA", "type": "hit", "avg": ".205", "h": 9, "hr": 0, "rbi": 0, "sb": 0, "ops": ".536"},
]

MATSUI_HIDEKI_YEARLY = [
    {"year": 2003, "team": "NYY", "type": "hit", "avg": ".287", "h": 179, "hr": 16, "rbi": 106, "sb": 2, "ops": ".788"},
    {"year": 2004, "team": "NYY", "type": "hit", "avg": ".298", "h": 174, "hr": 31, "rbi": 108, "sb": 3, "ops": ".912"},
    {"year": 2005, "team": "NYY", "type": "hit", "avg": ".305", "h": 192, "hr": 23, "rbi": 116, "sb": 2, "ops": ".868"},
    {"year": 2006, "team": "NYY", "type": "hit", "avg": ".302", "h": 53, "hr": 8, "rbi": 29, "sb": 0, "ops": ".883"},
    {"year": 2007, "team": "NYY", "type": "hit", "avg": ".285", "h": 156, "hr": 25, "rbi": 103, "sb": 0, "ops": ".852"},
    {"year": 2008, "team": "NYY", "type": "hit", "avg": ".294", "h": 99, "hr": 9, "rbi": 45, "sb": 0, "ops": ".792"},
    {"year": 2009, "team": "NYY", "type": "hit", "avg": ".274", "h": 117, "hr": 28, "rbi": 90, "sb": 0, "ops": ".876"},
    {"year": 2010, "team": "LAA", "type": "hit", "avg": ".274", "h": 132, "hr": 21, "rbi": 84, "sb": 0, "ops": ".820"},
    {"year": 2011, "team": "OAK", "type": "hit", "avg": ".251", "h": 117, "hr": 12, "rbi": 72, "sb": 0, "ops": ".720"},
    {"year": 2012, "team": "TB", "type": "hit", "avg": ".147", "h": 14, "hr": 2, "rbi": 7, "sb": 0, "ops": ".459"},
]

NOMO_YEARLY = [
    {"year": 1995, "team": "LAD", "type": "pit", "w": 13, "l": 6, "era": "2.54", "so": 236, "ip": "191.1", "whip": "1.06"},
    {"year": 1996, "team": "LAD", "type": "pit", "w": 16, "l": 11, "era": "3.19", "so": 234, "ip": "228.1", "whip": "1.16"},
    {"year": 1997, "team": "LAD", "type": "pit", "w": 14, "l": 12, "era": "4.25", "so": 233, "ip": "207.1", "whip": "1.39"},
    {"year": 1998, "team": "LAD/NYM", "type": "pit", "w": 6, "l": 12, "era": "4.92", "so": 152, "ip": "162.2", "whip": "1.45"},
    {"year": 1999, "team": "MIL", "type": "pit", "w": 12, "l": 8, "era": "4.54", "so": 161, "ip": "176.1", "whip": "1.47"},
    {"year": 2000, "team": "DET", "type": "pit", "w": 8, "l": 12, "era": "4.74", "so": 181, "ip": "190.0", "whip": "1.39"},
    {"year": 2001, "team": "BOS", "type": "pit", "w": 13, "l": 10, "era": "4.50", "so": 220, "ip": "198.0", "whip": "1.29"},
    {"year": 2002, "team": "LAD", "type": "pit", "w": 16, "l": 6, "era": "3.39", "so": 193, "ip": "220.1", "whip": "1.22"},
    {"year": 2003, "team": "LAD", "type": "pit", "w": 16, "l": 13, "era": "3.09", "so": 177, "ip": "218.1", "whip": "1.21"},
    {"year": 2004, "team": "LAD", "type": "pit", "w": 4, "l": 11, "era": "8.25", "so": 54, "ip": "84.0", "whip": "1.86"},
    {"year": 2005, "team": "TB", "type": "pit", "w": 5, "l": 8, "era": "7.24", "so": 59, "ip": "100.2", "whip": "1.79"},
    {"year": 2008, "team": "KC", "type": "pit", "w": 0, "l": 0, "era": "18.69", "so": 18, "ip": "8.2", "whip": "3.46"},
]

TANAKA_YEARLY = [
    {"year": 2014, "team": "NYY", "type": "pit", "w": 13, "l": 5, "era": "2.77", "so": 141, "ip": "136.1", "whip": "1.06"},
    {"year": 2015, "team": "NYY", "type": "pit", "w": 12, "l": 7, "era": "3.51", "so": 139, "ip": "154.0", "whip": "0.99"},
    {"year": 2016, "team": "NYY", "type": "pit", "w": 14, "l": 4, "era": "3.07", "so": 165, "ip": "199.2", "whip": "1.08"},
    {"year": 2017, "team": "NYY", "type": "pit", "w": 13, "l": 12, "era": "4.74", "so": 194, "ip": "178.1", "whip": "1.24"},
    {"year": 2018, "team": "NYY", "type": "pit", "w": 12, "l": 6, "era": "3.75", "so": 159, "ip": "156.0", "whip": "1.13"},
    {"year": 2019, "team": "NYY", "type": "pit", "w": 11, "l": 9, "era": "4.45", "so": 149, "ip": "182.0", "whip": "1.24"},
    {"year": 2020, "team": "NYY", "type": "pit", "w": 3, "l": 3, "era": "3.56", "so": 44, "ip": "48.0", "whip": "1.17"},
]

UEHARA_YEARLY = [
    {"year": 2009, "team": "BAL", "type": "pit", "w": 2, "l": 4, "era": "4.05", "so": 48, "ip": "66.2", "whip": "1.05"},
    {"year": 2010, "team": "BAL", "type": "pit", "w": 1, "l": 2, "era": "2.86", "so": 55, "ip": "44.0", "whip": "0.95"},
    {"year": 2011, "team": "BAL/TEX", "type": "pit", "w": 2, "l": 4, "era": "1.72", "so": 85, "ip": "65.1", "whip": "0.71"},
    {"year": 2012, "team": "TEX", "type": "pit", "w": 1, "l": 2, "era": "1.75", "so": 43, "ip": "36.0", "whip": "0.64"},
    {"year": 2013, "team": "BOS", "type": "pit", "w": 4, "l": 1, "era": "1.09", "so": 101, "ip": "74.1", "whip": "0.57"},
    {"year": 2014, "team": "BOS", "type": "pit", "w": 6, "l": 5, "era": "2.52", "so": 80, "ip": "64.1", "whip": "0.92"},
    {"year": 2015, "team": "BOS", "type": "pit", "w": 2, "l": 3, "era": "2.23", "so": 47, "ip": "40.1", "whip": "1.04"},
    {"year": 2016, "team": "BOS", "type": "pit", "w": 2, "l": 3, "era": "3.45", "so": 63, "ip": "47.0", "whip": "0.91"},
    {"year": 2017, "team": "CHC", "type": "pit", "w": 2, "l": 2, "era": "3.98", "so": 40, "ip": "43.0", "whip": "1.21"},
]

KURODA_YEARLY = [
    {"year": 2008, "team": "LAD", "type": "pit", "w": 9, "l": 10, "era": "3.73", "so": 116, "ip": "183.1", "whip": "1.22"},
    {"year": 2009, "team": "LAD", "type": "pit", "w": 8, "l": 7, "era": "3.76", "so": 105, "ip": "117.1", "whip": "1.16"},
    {"year": 2010, "team": "LAD", "type": "pit", "w": 11, "l": 13, "era": "3.39", "so": 159, "ip": "196.1", "whip": "1.16"},
    {"year": 2011, "team": "LAD", "type": "pit", "w": 13, "l": 16, "era": "3.07", "so": 161, "ip": "202.0", "whip": "1.21"},
    {"year": 2012, "team": "NYY", "type": "pit", "w": 16, "l": 11, "era": "3.32", "so": 167, "ip": "219.2", "whip": "1.17"},
    {"year": 2013, "team": "NYY", "type": "pit", "w": 11, "l": 13, "era": "3.31", "so": 150, "ip": "201.1", "whip": "1.16"},
    {"year": 2014, "team": "NYY", "type": "pit", "w": 11, "l": 9, "era": "3.71", "so": 146, "ip": "199.0", "whip": "1.20"},
]

PLAYERS = [
    # ===== MLB - Two-Way =====
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
    },
    # ===== MLB - Position Players =====
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
    },
    # ===== MLB - Pitchers =====
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
    },
    # ===== AAA (Triple-A) =====
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
    },
    # ===== FORMER (過去のMLB所属) =====
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
print(f"Generated {len(PLAYERS)} players: MLB={mlb} AAA={aaa} FORMER={former}")
