#!/usr/bin/env python3
"""Generate player JSON files for SakuraBall — MLB + 3A Japanese players."""
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
    {
        "key": "fujinami",
        "name_jp": "藤浪晋太郎", "name_en": "Shintaro Fujinami",
        "team_jp": "ニューヨーク・メッツ", "team_en": "New York Mets", "team_short": "NYM",
        "league": "NL", "level": "MLB", "type": "pitcher",
        "position_jp": "中継ぎ投手", "position_en": "Relief Pitcher",
        "basic": {"pitching": {"era": "4.50", "w": 1, "l": 0, "so": 15, "whip": "1.50", "ip": "12.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 52.0, "ba": ".240", "whiff": 28.0, "hard_hit": 40.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 28.5, "ba": ".200", "whiff": 35.0, "hard_hit": 32.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 19.5, "ba": ".210", "whiff": 32.0, "hard_hit": 30.0},
            ],
        },
    },
    # ===== AAA (Triple-A) =====
    {
        "key": "uwasawa",
        "name_jp": "上沢直之", "name_en": "Naoyuki Uwasawa",
        "team_jp": "ダーラム・ブルズ (3A)", "team_en": "Durham Bulls (AAA)", "team_short": "DUR",
        "league": "AAA", "level": "AAA", "type": "pitcher",
        "position_jp": "先発投手", "position_en": "Starting Pitcher",
        "basic": {"pitching": {"era": "3.85", "w": 2, "l": 1, "so": 20, "whip": "1.25", "ip": "22.0"}},
        "savant": {
            "pitch_arsenal": [
                {"pitch": "FF", "jp": "4シーム", "en": "4-Seam Fastball", "usage": 42.0, "ba": ".265", "whiff": 18.0, "hard_hit": 42.0},
                {"pitch": "FS", "jp": "スプリット", "en": "Splitter", "usage": 25.5, "ba": ".210", "whiff": 32.0, "hard_hit": 30.0},
                {"pitch": "SL", "jp": "スライダー", "en": "Slider", "usage": 18.0, "ba": ".235", "whiff": 28.0, "hard_hit": 35.0},
                {"pitch": "CU", "jp": "カーブ", "en": "Curveball", "usage": 14.5, "ba": ".220", "whiff": 25.0, "hard_hit": 32.0},
            ],
        },
    },
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
]

UPDATED = "2026-04-25"
for p in PLAYERS:
    p.setdefault("updated_at", UPDATED)
    path = OUT / f"{p['key']}.json"
    path.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generated {len(PLAYERS)} players at {OUT}")
print("MLB:", sum(1 for p in PLAYERS if p["level"] == "MLB"))
print("AAA:", sum(1 for p in PLAYERS if p["level"] == "AAA"))
