#!/usr/bin/env python3
"""Generate player JSON files for SakuraBall — MLB + 3A + 過去のMLB."""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "src" / "content" / "players"
OUT.mkdir(parents=True, exist_ok=True)

PLAYERS = [
    # ===== MLB - Two-Way =====
    {
        "key": "ohtani",
        "name_jp": "大谷翔平", "name_en": "Shohei Ohtani",
        "team_jp": "ロサンゼルス・ドジャース", "team_en": "Los Angeles Dodgers", "team_short": "LAD",
        "league": "NL", "level": "MLB", "type": "two_way",
        "position_jp": "指名打者 / 投手", "position_en": "DH / Pitcher",
        "basic": {
            "hitting": {"avg": ".245", "hr": 5, "rbi": 12, "obp": ".380", "ops": ".900", "sb": 3},
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
        "basic": {"hitting": {"avg": ".276", "hr": 4, "rbi": 11, "obp": ".355", "ops": ".830", "sb": 1}},
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
        "basic": {"hitting": {"avg": ".291", "hr": 2, "rbi": 8, "obp": ".345", "ops": ".780", "sb": 0}},
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
        "basic": {"hitting": {"avg": ".253", "hr": 10, "rbi": 19, "obp": ".420", "ops": ".992", "sb": 0}},
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
        "basic": {"pitching": {"era": "2.50", "w": 0, "l": 0, "so": 12, "whip": "1.05", "ip": "10.2"}},
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
        "basic": {"hitting": {"avg": ".311", "hr": 117, "rbi": 780, "obp": ".355", "ops": ".757", "sb": 509}},
    },
    {
        "key": "matsui-hideki",
        "name_jp": "松井秀喜", "name_en": "Hideki Matsui",
        "team_jp": "ニューヨーク・ヤンキース", "team_en": "New York Yankees", "team_short": "NYY",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手 / 指名打者", "position_en": "OF / DH",
        "mlb_years": "2003-2012",
        "current_status_jp": "2012年引退", "current_status_en": "Retired (2012)",
        "basic": {"hitting": {"avg": ".282", "hr": 175, "rbi": 760, "obp": ".360", "ops": ".822", "sb": 7}},
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
    },
    {
        "key": "uehara",
        "name_jp": "上原浩治", "name_en": "Koji Uehara",
        "team_jp": "ボストン・レッドソックス", "team_en": "Boston Red Sox", "team_short": "BOS",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2009-2017",
        "current_status_jp": "2019年引退", "current_status_en": "Retired (2019)",
        "basic": {"pitching": {"era": "2.66", "w": 22, "l": 26, "so": 562, "whip": "0.89", "ip": "440.2"}},
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
        "basic": {"hitting": {"avg": ".285", "hr": 35, "rbi": 192, "obp": ".350", "ops": ".743", "sb": 79}},
    },
    {
        "key": "fukudome",
        "name_jp": "福留孝介", "name_en": "Kosuke Fukudome",
        "team_jp": "シカゴ・カブス", "team_en": "Chicago Cubs", "team_short": "CHC",
        "league": "NL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2008-2012",
        "current_status_jp": "2022年引退", "current_status_en": "Retired (2022)",
        "basic": {"hitting": {"avg": ".258", "hr": 42, "rbi": 195, "obp": ".359", "ops": ".739", "sb": 13}},
    },
    {
        "key": "iwamura",
        "name_jp": "岩村明憲", "name_en": "Akinori Iwamura",
        "team_jp": "タンパベイ・レイズ", "team_en": "Tampa Bay Rays", "team_short": "TB",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "二塁手 / 三塁手", "position_en": "2B / 3B",
        "mlb_years": "2007-2010",
        "current_status_jp": "2017年引退", "current_status_en": "Retired (2017)",
        "basic": {"hitting": {"avg": ".267", "hr": 16, "rbi": 145, "obp": ".346", "ops": ".710", "sb": 21}},
    },
    {
        "key": "hirano",
        "name_jp": "平野佳寿", "name_en": "Yoshihisa Hirano",
        "team_jp": "アリゾナ・ダイヤモンドバックス", "team_en": "Arizona Diamondbacks", "team_short": "ARI",
        "league": "NL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2018-2020",
        "current_status_jp": "オリックス・バファローズ所属", "current_status_en": "Now with Orix (NPB)",
        "basic": {"pitching": {"era": "4.40", "w": 6, "l": 7, "so": 130, "whip": "1.32", "ip": "133.0"}},
    },
    {
        "key": "tsutsugo",
        "name_jp": "筒香嘉智", "name_en": "Yoshitomo Tsutsugo",
        "team_jp": "タンパベイ・レイズ", "team_en": "Tampa Bay Rays", "team_short": "TB",
        "league": "AL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手 / 一塁手", "position_en": "OF / 1B",
        "mlb_years": "2020-2022",
        "current_status_jp": "横浜DeNAベイスターズ所属", "current_status_en": "Now with Yokohama DeNA (NPB)",
        "basic": {"hitting": {"avg": ".211", "hr": 14, "rbi": 53, "obp": ".311", "ops": ".677", "sb": 0}},
    },
    {
        "key": "akiyama",
        "name_jp": "秋山翔吾", "name_en": "Shogo Akiyama",
        "team_jp": "シンシナティ・レッズ", "team_en": "Cincinnati Reds", "team_short": "CIN",
        "league": "NL", "level": "FORMER", "type": "batter",
        "position_jp": "外野手", "position_en": "Outfielder",
        "mlb_years": "2020-2021",
        "current_status_jp": "広島東洋カープ所属", "current_status_en": "Now with Hiroshima (NPB)",
        "basic": {"hitting": {"avg": ".224", "hr": 0, "rbi": 16, "obp": ".300", "ops": ".574", "sb": 6}},
    },
    {
        "key": "fujinami",
        "name_jp": "藤浪晋太郎", "name_en": "Shintaro Fujinami",
        "team_jp": "オークランド・アスレチックス", "team_en": "Oakland Athletics", "team_short": "OAK",
        "league": "AL", "level": "FORMER", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "mlb_years": "2023-2024",
        "current_status_jp": "NPB復帰",
        "current_status_en": "Returned to NPB",
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
