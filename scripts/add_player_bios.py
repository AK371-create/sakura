#!/usr/bin/env python3
"""Add bio_jp / bio_en to player JSONs (1 sentence: feature + career highlight)."""
import json
from pathlib import Path

PLAYERS = Path(__file__).parent.parent / "src" / "content" / "players"

BIOS = {
    # Active MLB
    "ohtani":         ("投打二刀流のスーパースター。2024年に54HR/130打点/59盗塁でMVPと50/50を達成。",
                       "Two-way superstar. 2024 NL MVP with 54HR/130RBI/59SB (50/50 club)."),
    "yamamoto":       ("精密な制球と高速カーブが武器の右腕。NPB3年連続沢村賞からドジャースへ。",
                       "Right-hander with elite command and high-spin curve. Three NPB Sawamura Awards before joining LAD."),
    "imanaga":        ("低リリースから伸びる4シームとスプリットの組合せ。2024年新人王候補で15勝。",
                       "Low-release rising 4-seam plus splitter. 2024 ROY runner-up with 15 wins and 2.91 ERA."),
    "darvish":        ("10種類超の球種を操る支配的右腕。2013年AL最多奪三振 (277K) を記録。",
                       "Dominant righty with 10+ pitch types. Led the AL with 277 strikeouts in 2013."),
    "senga":          ("お化けフォークの使い手。2023年ERA 2.98、202奪三振でメッツに定着。",
                       "Splits a 'ghost forkball' that makes hitters miss. 2.98 ERA / 202 K in his 2023 debut."),
    "sasaki":         ("100mph超の4シームと縦に落ちるフォーク。NPB完全試合と13連続奪三振の若き怪物。",
                       "100+ mph 4-seam paired with a sharp forkball. Threw NPB's only perfect game with 13 straight K's."),
    "kikuchi":        ("左腕パワーピッチャー。2024年に9勝+206奪三振でキャリアハイ。",
                       "Power lefty. Career-high 206 strikeouts and 9 wins in 2024."),
    "matsui-yuki":    ("NPB通算最年少200セーブ達成。2024年パドレス入りで左の中継ぎ重要ピース。",
                       "Youngest NPB pitcher to 200 saves. Joined SD's bullpen as a setup lefty in 2024."),
    "suzuki":         ("広角に長打を打てる外野手。2023年に20HR/74打点/.842 OPSでブレイク。",
                       "Power-to-all-fields outfielder. Breakout 2023 with 20 HR / 74 RBI / .842 OPS."),
    "yoshida":        ("MLB屈指のコンタクト能力。2023年に.289/15HR/72打点でルーキー級活躍。",
                       "Elite contact bat. 2023 debut: .289 / 15 HR / 72 RBI in 140 games."),

    # AAA
    "saito":          ("160km/h超の速球を持つ右腕。Giants傘下のサクラメントで再起を狙う。",
                       "Right-hander with 100 mph heat. Working back to MLB through Giants' AAA Sacramento."),
    "ogasawara":      ("コントロールに優れる左腕先発。Nationals傘下AAAで2025年メジャー昇格を経験。",
                       "Lefty starter with command. Reached MLB briefly with Washington in 2025."),

    # FORMER — Legends
    "ichiro":         ("10年連続200安打+3割の天才アベレージヒッター。2004年にMLB単独記録262安打+打率.372。",
                       "10 straight 200-hit, .300+ seasons. Set the single-season hits record (262) with a .372 average in 2004."),
    "nomo":           ("トルネード投法でMLBに道を切り拓いたパイオニア。1995年新人王+2度のノーヒッター。",
                       "Pioneer of the modern Japanese-MLB era with his tornado windup. 1995 ROY and two no-hitters."),
    "matsui-hideki":  ("ヤンキース時代の中軸打者。2009年ワールドシリーズMVP (打率.615/3HR/8打点)。",
                       "Yankees middle-of-the-order presence. 2009 World Series MVP (.615 / 3 HR / 8 RBI)."),

    # FORMER — Recently retired/returned
    "uehara":         ("精密な制球の中継ぎ。2013年Red Soxで歴史的WHIP 0.57とALCS MVP/WS制覇。",
                       "Pinpoint relief ace. Historic 0.57 WHIP for the 2013 Red Sox, ALCS MVP and World Series ring."),
    "kuroda":         ("Yankees-Dodgersの先発で活躍した職人。2014年MLB通算79勝で日本に帰国・引退。",
                       "Reliable starter for the Dodgers and Yankees. Retired with 79 MLB wins after returning to Hiroshima."),
    "tanaka":         ("スプリッターで奪三振を量産。2014年AL ROY 2位 (13-5/2.77)、Yankees通算78勝。",
                       "Splitter specialist. 2014 AL ROY runner-up (13-5/2.77), 78 career wins as a Yankee."),
    "matsuzaka":      ("怪物伝説と称された右腕。2007年Red Sox入団、2008年に18勝3敗でMLB制覇。",
                       "The legendary 'Monster of the Lost Decade'. 18-3 in 2008 helped Boston win the World Series."),
    "aoki":           ("選球眼と走力の外野手。2014年KCのWS進出に貢献し、MLB通算3割打者級。",
                       "Disciplined contact-hitting outfielder. Helped KC reach the 2014 World Series."),
    "fukudome":       ("カブス時代の左の長距離砲。2008年MLBオールスター選出。",
                       "Cubs power-hitting outfielder. 2008 MLB All-Star."),
    "iwamura":        ("Rays 2008年AL優勝の二塁手。2007年新人で打率.285の好スタート。",
                       "Rays 2B on the 2008 AL pennant team. .285 in his 2007 rookie season."),
    "hirano":         ("D-backsの中継ぎとして2018年AS出場 (ERA 2.44)。日本人初の救援投手オールスター。",
                       "D-backs setup man, 2018 All-Star (2.44 ERA). First Japanese reliever ever named to an All-Star team."),
    "tsutsugo":       ("Raysを中心に長距離砲として挑戦。2022年に横浜DeNAへ復帰。",
                       "Power threat across multiple MLB clubs. Returned to Yokohama (NPB) in 2022."),
    "akiyama":        ("NPB通算盗塁上位の俊足外野手。Reds 2020年に挑戦、2022年広島復帰。",
                       "Speedy outfielder, prolific NPB stolen-base leader. Cincinnati 2020-21, then back to Hiroshima."),
    "fujinami":       ("160km/h超の剛速球を持つが制球難に苦しむ。2023年A's→2024年Mets。",
                       "Triple-digit heat with command issues. Athletics 2023 → Mets 2024."),
    "maeda":          ("カッター主体のコントロール派。2020年AL Cy Young 2位、2026年から楽天。",
                       "Cutter-heavy control artist. 2020 AL Cy Young runner-up, returned to NPB Rakuten in 2026."),

    # FORMER — Older alumni
    "mac-suzuki":     ("わずか17歳で米国留学から這い上がった右腕。1996年Marinersで20歳MLBデビュー。",
                       "Right-hander who clawed up from a teen US dream. MLB debut at 20 with Seattle in 1996."),
    "tazawa":         ("Red Sox中継ぎとして9年で388試合登板。2013年WSメンバー。",
                       "Red Sox setup man for 9 years (388 games). 2013 World Series champion."),
    "sawamura":       ("独特の腕の振りでメジャー挑戦。Red Sox 2021年に登板。",
                       "Unique deceptive delivery. Pitched for Red Sox in 2021."),
    "ohka":           ("制球派の長身右腕。Expos先発として2002年18勝。",
                       "Tall control righty. 18-win season for the Expos in 2002."),
    "johjima":        ("日本人初のMLB捕手。Mariners 2006-2009で4年契約。",
                       "First Japanese-born MLB catcher. Four years with Seattle (2006-2009)."),
    "igawa":          ("Yankeesと5年30M契約も活かせず。MLBでは2年で2試合のみ。",
                       "Signed a 5-year/$30M deal with NYY but pitched in just 2 MLB games."),
    "kawasaki":       ("Bluejaysで2013年活躍したムードメーカー。明るいキャラクターで愛された。",
                       "Beloved Blue Jay infielder famous for his upbeat personality. Career-best year in 2013."),
    "taguchi":        ("Cardinals 2006年WS制覇メンバー。器用な代打外野手。",
                       "St. Louis Cardinals 2006 World Series champion. Versatile reserve outfielder."),
    "takahashi-h":    ("ベテラン左腕中継ぎ。Mets/Angels等で4シーズン。",
                       "Veteran lefty reliever. Four MLB seasons across Mets, Angels and others."),
    "otsuka":         ("2006年Rangers特殊救援。同年AL救援投手賞 (32セーブ/2.11 ERA)。",
                       "2006 AL Reliever of the Year with Texas (32 saves, 2.11 ERA)."),
    "fujikawa":       ("阪神タイガースのレジェンド。CubsでMLB挑戦も3シーズンで帰国。",
                       "Hanshin Tigers legend. Three injury-marred seasons with the Cubs before returning to NPB."),
    "nishioka":       ("Twins 2011年に脛骨骨折で苦戦、2年で日本に復帰。",
                       "Twins infielder hampered by leg injuries in 2011. Returned to NPB after two seasons."),
    "igarashi":       ("Mets/Pirates等3年。160km/h右腕として一時代築いた中継ぎ。",
                       "Three MLB seasons (Mets/Pirates). Hard-throwing setup arm."),
    "takatsu":        ("ChiSox 2004年AL中地区優勝の救援。2005年Mets移籍。",
                       "ChiSox closer-types contributor on the 2004 AL Central champ. Moved to Mets in 2005."),
    "kawakami":       ("Braves 2009-2010の先発。中日のエースだったがMLBでは伸び悩む。",
                       "Two-year Atlanta Braves starter. Star at Chunichi but struggled to translate to MLB."),
    "makita":         ("特殊なサイドハンドフォームのリリーバー。Padres 2018年に挑戦。",
                       "Submarine-style reliever. One season with San Diego (2018)."),
    "tadano":         ("日本人初の大学卒メジャー昇格。Indians 2004年に登板。",
                       "First Japanese collegiate-route MLB pitcher. Cleveland Indians, 2004."),
    "kida":           ("日本人初のメジャー登板を1999年Tigers戦で達成。複数球団を渡り歩く。",
                       "Made the first MLB appearance by a Japanese pitcher with the Tigers in 1999."),
    "yabu":           ("ベテラン右腕。2008年GiantsではERA 3.57で起用された。",
                       "Veteran righty. ERA 3.57 across 60+ games for the 2008 Giants."),
    "fukumori":       ("Rangers 2008年に挑戦するも8試合で帰国。NPB最多セーブの実績。",
                       "Pitched in 8 games for Texas in 2008 before returning. Held NPB's all-time saves mark."),
    "okajima":        ("Red Sox 2007年新人で活躍したサウスポー。WS制覇メンバー。",
                       "Red Sox 2007 ROY-vote receiver as a left-handed setup arm. WS champion."),
    "yoshii":         ("巨人のエースからMLBへ。Mets 1999年に12勝+ポストシーズン勝利投手。",
                       "Yomiuri Giants ace who won 12 for the 1999 Mets and pitched in October."),
    "sasaki-k":       ("'大魔神'の異名を持つ伝説のクローザー。Mariners 2000年AL最優秀新人 (37セーブ)。",
                       "'Daimajin' the legendary closer. 2000 AL Rookie of the Year with 37 saves for Seattle."),
    "wada":           ("Cubs 2014-2015年に先発。日本でのキャリアの方が長い左腕。",
                       "Lefty starter who pitched 1.5 seasons with the Cubs (2014-15)."),
    "iwakuma":        ("Mariners 2012-17のエース。2015年8月にノーヒッター達成。",
                       "Seattle ace 2012-17. Threw a no-hitter in August 2015."),
    "saito-t":        ("Dodgers 2007年に防御率1.40。日本人最年長デビューでMLB ALL-STAR。",
                       "Late-blooming closer with 1.40 ERA in 2007 for LA. Oldest Japanese MLB debutant; later All-Star."),
    "tanaka-k":       ("Giants 2013年に4試合のみのMLB経験。NPB日本ハム長期主軸。",
                       "Brief 4-game stint with SF in 2013. Long-time Hokkaido Nippon-Ham regular."),
    "shinjo":         ("派手な振る舞いで愛されたMets/Giants外野手。2002年WS出場。",
                       "Flamboyant Mets/Giants outfielder. Played in the 2002 World Series with SF."),
    "nakamura":       ("Dodgers 2005年に17試合のみのMLB挑戦。NPBでは強打の三塁手。",
                       "Brief 17-game Dodgers stint in 2005. Power-hitting third baseman in NPB."),
}


def main():
    updated = 0
    for f in sorted(PLAYERS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        key = d.get("key")
        if key not in BIOS:
            continue
        jp, en = BIOS[key]
        d["bio_jp"] = jp
        d["bio_en"] = en
        f.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        updated += 1
        print(f"  + {key}")
    print(f"Updated {updated} players' bio")


if __name__ == "__main__":
    main()
