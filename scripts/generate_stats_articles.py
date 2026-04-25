#!/usr/bin/env python3
"""統計用語解説記事を生成 (新カテゴリ: stats / statcast)。
タグ・カテゴリ別に整理して既存記事と整合。"""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "src" / "content" / "articles"
OUT.mkdir(parents=True, exist_ok=True)
DATE = "2026-04-25"


def make_article(slug, category, tags, title_jp, title_en, summary_jp, summary_en, body_jp, body_en):
    return {
        "slug": slug,
        "date": DATE,
        "category": category,
        "tags": tags,
        "title_jp": title_jp,
        "title_en": title_en,
        "summary_jp": summary_jp,
        "summary_en": summary_en,
        "body_jp": body_jp,
        "body_en": body_en,
        "updated_at": DATE,
    }


ARTICLES = [
    # ===== 打撃基本 (5) =====
    make_article(
        "stats-batting-avg", "stats", ["statcast", "batting"],
        "打率 (AVG) とは",
        "What is Batting Average (AVG)?",
        "打率は最も古典的な打撃指標。安打数 ÷ 打数で算出される。",
        "Batting average is the most classic hitting metric: hits divided by at-bats.",
        [
            "打率(AVG)は安打を打数で割った値で、打者の安打を打つ確率を示す。.300以上は一流の目安、.350を超えれば首位打者級だ。",
            "計算式: 安打 ÷ 打数。四球・死球・犠打は打数に含めないため、選球眼の良い打者でも打数が増えにくい。",
            "イチローは2004年にMLB単独シーズン安打記録(262本)を樹立、打率.372で首位打者を獲得した。",
            "限界: 打率は単打もホームランも同じ1扱いで、長打力を反映しない。OPSやxwOBAと併用するのが一般的。"
        ],
        [
            "Batting average (AVG) divides hits by at-bats, showing how often a batter gets a hit. .300 is the standard for elite, .350+ is batting-title territory.",
            "Formula: hits / at-bats. Walks, hit-by-pitches, and sacrifices are not counted as at-bats, so disciplined hitters don't accumulate at-bats as quickly.",
            "Ichiro set the MLB single-season hits record (262) in 2004 with a .372 average, winning the batting title.",
            "Limitations: AVG treats singles and home runs equally, missing power. Pair it with OPS or xwOBA."
        ],
    ),
    make_article(
        "stats-batting-obp", "stats", ["statcast", "batting"],
        "出塁率 (OBP) とは",
        "What is On-Base Percentage (OBP)?",
        "打席に立った時に塁に出る確率。打率に四球と死球を加味した出塁能力の総合指標。",
        "How often a batter reaches base, including walks and hit-by-pitches. The headline plate-discipline metric.",
        [
            "出塁率(OBP)は (安打 + 四球 + 死球) ÷ (打数 + 四球 + 死球 + 犠飛)。打率より出塁の機会全般を捉える。",
            ".330台が平均、.380以上で優秀、.400以上は MLB 屈指。",
            "出塁率が高い打者は得点機会を作るため、上位打線で起用される傾向がある。",
            "OBP は打率より「失点を防ぐ」観点で価値があり、Moneyball 以降の評価軸として定着した。"
        ],
        [
            "OBP = (Hits + BB + HBP) / (AB + BB + HBP + SF). Captures all plate appearances ending on base.",
            ".330s is league average, .380+ is excellent, .400+ is elite among MLB.",
            "High-OBP hitters create scoring chances and tend to bat at the top of the order.",
            "OBP became a foundational metric post-Moneyball, valued for its tight correlation with team runs."
        ],
    ),
    make_article(
        "stats-batting-slg", "stats", ["statcast", "batting"],
        "長打率 (SLG) とは",
        "What is Slugging Percentage (SLG)?",
        "打数あたりの塁打数。単打1・二塁打2・三塁打3・本塁打4と重み付け。",
        "Total bases per at-bat: singles=1, doubles=2, triples=3, HR=4. Pure power output.",
        [
            "長打率(SLG)は (単打 + 二塁打×2 + 三塁打×3 + 本塁打×4) ÷ 打数。打者の長打力を直接表す。",
            "MLB平均は .400 前後、.500を超えれば強打者、.600以上は怪物級。",
            "本塁打が多い打者ほどSLGは高くなるが、二塁打・三塁打を量産する Doubles Hitter (例: 鈴木誠也) も .500 近くを狙える。",
            "SLGはOBPと組み合わせてOPS(=OBP+SLG)として扱われることが多い。"
        ],
        [
            "SLG = (1B + 2B×2 + 3B×3 + HR×4) / AB. Direct measure of power.",
            "MLB average is around .400; .500+ is a strong slugger, .600+ is monster territory.",
            "Big home run hitters lead SLG, but doubles hitters (like Suzuki) can approach .500 too.",
            "SLG is often combined with OBP to form OPS (= OBP + SLG)."
        ],
    ),
    make_article(
        "stats-batting-ops", "stats", ["statcast", "batting"],
        "OPS とは",
        "What is OPS?",
        "OBP + SLG。出塁能力と長打力を一つにまとめた、最も一般的な総合打撃指標。",
        "OBP + SLG combined — the most popular all-in-one offensive metric.",
        [
            "OPSは出塁率と長打率の単純な和。例: OBP .380 + SLG .500 → OPS .880。",
            ".700前後がMLB平均、.800で良打者、.900で強打者、1.000超えはMVP級。",
            "計算が直感的で野球解説でも頻出する。ただし出塁と長打を等価値に扱うため、より精密にはwOBA/xwOBAが推奨される。",
            "大谷翔平は2024年にOPS 1.036をマーク、ナ・リーグ首位を獲得した。"
        ],
        [
            "OPS is simply OBP + SLG. Example: .380 + .500 = .880.",
            ".700 is around average, .800 is good, .900 is great, 1.000+ is MVP-level.",
            "Easy to compute and widely cited. For more precise analysis, wOBA/xwOBA is preferred since OPS treats OBP and SLG as equally valued.",
            "Ohtani led the NL with a 1.036 OPS in 2024."
        ],
    ),
    make_article(
        "stats-batting-iso", "stats", ["statcast", "batting"],
        "ISO (純長打率) とは",
        "What is ISO (Isolated Power)?",
        "長打率から打率を引いた値。純粋な長打力を取り出す指標。",
        "SLG minus AVG — isolates raw power from contact ability.",
        [
            "ISO = SLG − AVG。例: AVG .280 SLG .500 → ISO .220。",
            ".200を超えれば強打者、.250以上で長距離砲、.300超えはMLB屈指。",
            "打率が低くてもISOが高ければホームランバッターとして機能する。",
            "ホームラン量産型打者の評価に有用で、AVG単独より打者タイプを正確に表す。"
        ],
        [
            "ISO = SLG − AVG. Example: .280 / .500 → ISO of .220.",
            ".200+ is a power hitter, .250+ is a slugger, .300+ is elite.",
            "A low-AVG hitter with a high ISO can still be valuable as a HR threat.",
            "Useful for distinguishing pure power hitters; complements AVG."
        ],
    ),
    # ===== 投手基本 (5) =====
    make_article(
        "stats-pitching-era", "stats", ["statcast", "pitching"],
        "防御率 (ERA) とは",
        "What is ERA?",
        "投手の最も基本的な指標。9イニングあたりの自責点。",
        "The most fundamental pitcher metric: earned runs per 9 innings.",
        [
            "防御率(ERA) = (自責点 × 9) ÷ 投球回。3.50以下で良好、2点台で一流、1点台はMLB屈指。",
            "「自責点」とは野手のエラーや捕逸が絡まない失点のことで、純粋に投手の責任とされるもの。",
            "ただし、ERAは球場・守備・運の影響を受けるため、FIPなど守備独立指標と併用するのが現代分析の主流。",
            "野茂英雄は1995年にナ・リーグ最多奪三振(236)でERA 2.54をマーク、新人王に輝いた。"
        ],
        [
            "ERA = (Earned Runs × 9) / Innings Pitched. Sub-3.50 is good, 2.xx is elite, 1.xx is rarefied.",
            "An 'earned run' excludes runs scoring due to fielding errors or passed balls.",
            "ERA is influenced by ballpark, defense, and luck. Modern analysis pairs it with FIP for a defense-independent view.",
            "Hideo Nomo won the 1995 NL Rookie of the Year with a 2.54 ERA and 236 strikeouts."
        ],
    ),
    make_article(
        "stats-pitching-whip", "stats", ["statcast", "pitching"],
        "WHIP とは",
        "What is WHIP?",
        "1イニングあたりに許す走者数 (与四球 + 被安打)。",
        "Walks + Hits per Inning Pitched — baserunners allowed per inning.",
        [
            "WHIP = (与四球 + 被安打) ÷ 投球回。1.30以下で良好、1.10以下で一流、1.00未満は怪物級。",
            "ERAは失点だが、WHIPは「走者を許さない能力」を直接示す。長期的にはERAより安定する傾向。",
            "上原浩治は2013年にWHIP 0.57という歴史的数字を残した(レッドソックスのリリーフ)。",
            "計算がシンプルで、リリーフ・先発両方に応用可能。"
        ],
        [
            "WHIP = (BB + Hits) / IP. Sub-1.30 is good, 1.10 is elite, sub-1.00 is exceptional.",
            "Where ERA tracks runs, WHIP captures the rate of allowing baserunners — often more stable over time.",
            "Koji Uehara posted a historic 0.57 WHIP in 2013 (Boston relief).",
            "Simple to compute and applies equally to starters and relievers."
        ],
    ),
    make_article(
        "stats-pitching-k9-bb9", "stats", ["statcast", "pitching"],
        "K/9 と BB/9 とは",
        "What are K/9 and BB/9?",
        "9イニング換算の奪三振数と与四球数。投手の支配力を端的に示す。",
        "Strikeouts and walks per 9 innings — quick gauge of dominance and command.",
        [
            "K/9 = (奪三振 × 9) ÷ 投球回、BB/9 も同様。",
            "K/9 が 9 を超えれば強い投手、12+ なら超一流。BB/9 は 2.0 以下が理想。",
            "K/BB (K/9 ÷ BB/9 ではなく純粋な奪三振÷与四球比) も併用される。3.0以上が良好、5.0+ で一流。",
            "ダルビッシュ有は2013年にAL最多奪三振(277)を記録、K/9 11.9 という支配力を見せた。"
        ],
        [
            "K/9 = (Strikeouts × 9) / IP, with BB/9 computed the same way.",
            "K/9 above 9 is strong; 12+ is elite. BB/9 under 2.0 is ideal.",
            "K/BB ratio is also useful (above 3.0 is good, 5.0+ is elite).",
            "Yu Darvish led the AL with 277 strikeouts in 2013, posting an 11.9 K/9."
        ],
    ),
    make_article(
        "stats-pitching-fip", "stats", ["statcast", "pitching"],
        "FIP (守備独立投手指標) とは",
        "What is FIP?",
        "投手が「自分でコントロールできる」結果(三振/四球/本塁打)だけで防御率風に計算した指標。",
        "An ERA-style metric using only outcomes a pitcher controls: strikeouts, walks, home runs.",
        [
            "FIP = (13×HR + 3×BB − 2×K) ÷ IP + 定数。守備の影響を排除した「真の投手力」とされる。",
            "ERAより低い → 運/守備に恵まれている。ERAより高い → 運/守備が悪い。",
            "三振が多くBB・HRが少ない投手はFIPが低くなる。長期的にはERAがFIPに収束する傾向。",
            "現代の年俸査定や予測モデルではFIPやxFIP、SIERAが重視される。"
        ],
        [
            "FIP = (13×HR + 3×BB − 2×K) / IP + constant. Strips out defense and luck.",
            "FIP below ERA suggests good luck/defense; above ERA suggests bad luck/defense.",
            "Pitchers with high K, low BB and HR have low FIP. ERA tends to regress toward FIP over time.",
            "Modern projection systems favor FIP/xFIP/SIERA over raw ERA."
        ],
    ),
    make_article(
        "stats-pitching-sv-hld", "stats", ["statcast", "pitching"],
        "セーブ (SV) と ホールド (HLD) の違い",
        "Saves (SV) vs. Holds (HLD)",
        "クローザーとセットアッパーを区別する役割別指標。",
        "Stats that distinguish closers (saves) from setup men (holds).",
        [
            "セーブ: リード時に登板し最終アウトまで投げ切ること。3点リード以下、走者あり、または同点ピンチで登板して逃げ切るのが代表条件。",
            "ホールド: リード時に登板し、リードを保ったまま降板すること(救援に引き継ぐ)。9回完全制圧でなくても評価される。",
            "上原浩治はBOS時代に通算95セーブ(2013年AL最多21)、松井裕樹はパドレス2024年9ホールドで起用された。",
            "両指標とも「機会」が必要なため、クローザー/セットアッパーの起用ポリシー次第で数字が左右される。"
        ],
        [
            "Save: protect a lead from entry through the final out — typically up by 3 or fewer with runners on or in a tie-break situation.",
            "Hold: enter with a lead and exit before the final out while preserving it. Setup men's bread and butter.",
            "Koji Uehara collected 95 saves in his Red Sox tenure (21 in 2013); Yuki Matsui posted 9 holds with the Padres in 2024.",
            "Both stats depend on opportunities — bullpen role assignment heavily affects the numbers."
        ],
    ),
    # ===== Statcast (5) =====
    make_article(
        "stats-statcast-hardhit", "stats", ["statcast", "batting"],
        "Hard-Hit率とは",
        "What is Hard-Hit %?",
        "打球速度95mph以上の打球の割合。Barrel率の前提となる強い打球の頻度。",
        "Percentage of batted balls with exit velocity 95+ mph — the precursor to Barrel rate.",
        [
            "Hard-Hit率は95mph以上の打球の比率。MLB平均は40%前後、50%超えで強打者、60%超えで MLB屈指。",
            "Barrel率は「強くかつ理想角度」で打った打球だが、Hard-Hit率は角度を問わない。打球の純粋な強さを測る。",
            "ゴロでも95mph超えなら Hard-Hit にカウントされる。長打にならなくても投手にプレッシャーをかける指標。",
            "Hard-Hit率が高くBarrel率も高い打者は理想形(例: 大谷翔平、ジャッジ)。"
        ],
        [
            "Hard-Hit% is the share of batted balls 95+ mph. MLB average is ~40%, 50%+ is strong, 60%+ is elite.",
            "Unlike Barrel%, Hard-Hit% doesn't require an ideal launch angle — pure raw contact strength.",
            "Even ground balls count if hit hard enough, signaling pressure on opposing defenses.",
            "Hitters strong in both Hard-Hit% and Barrel% are the ideal (Ohtani, Judge, etc.)."
        ],
    ),
    make_article(
        "stats-statcast-launch-angle", "stats", ["statcast", "batting"],
        "打球角度 (Launch Angle) とは",
        "What is Launch Angle?",
        "打球が水平からどれだけ上に飛んだかの角度。長打を生む最重要パラメータの一つ。",
        "The vertical angle of a batted ball off the bat — a key driver of extra-base hits.",
        [
            "打球角度は水平を0°、真上を90°として計測される。一般に10°〜25°で打球が伸び、本塁打になりやすい。",
            "10°未満はゴロが多くなり、35°以上はフライ/ポップが増えて凡打になる。",
            "最適角度は打球速度と相関する。速い打球ほど許容角度の幅が広い。",
            "近年は『フライボール革命』で打者が意識的にLAを上げる傾向(平均LAは2010年代から徐々に上昇)。"
        ],
        [
            "Launch angle measures the vertical angle of contact — 0° is horizontal, 90° is straight up. Most extra-base hits come in the 10-25° range.",
            "Below 10° tends to produce ground balls; above 35° leads to flies/pop-ups.",
            "The ideal angle correlates with exit velocity — harder hits expand the productive angle range.",
            "The 'fly-ball revolution' has gradually pushed average LA upward since the 2010s."
        ],
    ),
    make_article(
        "stats-statcast-xba-xslg", "stats", ["statcast", "batting"],
        "xBA / xSLG (期待値統計) とは",
        "What are xBA and xSLG?",
        "打球速度と角度から「本来期待される」打率と長打率。実数値との差で運の影響を見る。",
        "Expected AVG and SLG based on exit velocity and launch angle — strip out luck.",
        [
            "xBA は打球速度・角度・走力から計算される打率の期待値。打者の打球内容を運抜きで評価する。",
            "xSLG も同様で、長打力の期待値を出す。実SLG > xSLG なら運に恵まれた、実SLG < xSLG なら不運。",
            "サンプルサイズが大きくなるほど、実値はxBA/xSLGに収束する。シーズン途中で乖離が大きい打者は今後の調整候補。",
            "xwOBA も同じ系統で、出塁全般の期待値を表す総合指標。"
        ],
        [
            "xBA is the expected batting average based on exit velocity, launch angle, and (for some plays) sprint speed — strips out luck.",
            "xSLG analogously projects expected slugging. Actual SLG > xSLG means lucky; actual < xSLG means unlucky.",
            "Over larger samples, actual stats regress toward xBA/xSLG. Big mid-season gaps flag likely regression.",
            "xwOBA extends the same idea to overall offensive value."
        ],
    ),
    make_article(
        "stats-statcast-whiff", "stats", ["statcast", "pitching"],
        "Whiff% (空振り率) とは",
        "What is Whiff %?",
        "打者がスイングして空振りした割合。投手の決め球の支配力指標。",
        "Percentage of swings that miss — how dominant a pitch's swing-and-miss profile is.",
        [
            "Whiff% = 空振り回数 ÷ スイング回数。MLB平均は25%前後、35%超えで一流、45%以上はMLB屈指。",
            "球種別に見ると価値が分かる。スプリッターやスライダーで40%超えれば「決め球」級。",
            "今永昇太のスプリッターは2024年にWhiff 41.9%を記録した。",
            "ストライクゾーン外への誘い球(chase)が多いとWhiff%は上がる。"
        ],
        [
            "Whiff% = whiffs / swings. MLB average is ~25%, 35%+ is elite, 45%+ is rarefied.",
            "Per-pitch breakdown reveals putaway pitches — splitters and sliders above 40% are 'wipeout' offerings.",
            "Imanaga's splitter posted a 41.9% whiff rate in 2024.",
            "Inducing chases (out-of-zone swings) tends to lift Whiff%."
        ],
    ),
    make_article(
        "stats-statcast-spin-rate", "stats", ["statcast", "pitching"],
        "回転数 (Spin Rate) とは",
        "What is Spin Rate?",
        "ボールが1分間に回転する数(rpm)。球種ごとに最適レンジがあり、伸び・変化に直結。",
        "Revolutions per minute on the ball — directly affects movement profile by pitch type.",
        [
            "回転数は単位 rpm で計測。同じ95mphでも、4シーム高回転(2400+)は『伸び』てバットに当たりにくい。",
            "ライザー系4シームは2300-2700rpm、カーブは2700+rpm が望ましい。",
            "球種ごとの最適範囲があり、闇雲に高ければ良いわけではない(チェンジアップは低めが理想)。",
            "近年はスティッキー物質規制でMLB平均rpmが減少傾向。"
        ],
        [
            "Spin rate is measured in RPM. At the same 95 mph, a high-spin (2400+) 4-seamer 'rises' and is harder to hit.",
            "Riding 4-seamers want 2300-2700 RPM; curveballs benefit from 2700+ RPM.",
            "Each pitch type has an optimal band — higher isn't universally better (changeups prefer low spin).",
            "The 2021 sticky-substance crackdown lowered MLB average RPMs."
        ],
    ),
    # ===== 球種 (5) =====
    make_article(
        "stats-pitch-fourseam", "stats", ["statcast", "pitch-type"],
        "4シーム・ファストボール (FF)",
        "Four-Seam Fastball (FF)",
        "MLB最も基本的な速球。回転軸と回転数で『伸び』が変わる。",
        "The most common fastball in MLB. Movement profile depends on spin axis and rate.",
        [
            "4シームは縫い目を4本横切るように握る速球。回転数が高いと『ライズ』して見え、空振りを取りやすい。",
            "球速95mph以上で平均的に強い、98+で支配級。佐々木朗希・大谷翔平は100mph超えを連発する。",
            "高めゾーンに投げ込むと『浮き上がる』錯覚で空振り率が上がる(今永昇太の戦術)。",
            "近年はSeam-Shifted Wakeにより同じ4シームでも変化量が異なる現象が研究されている。"
        ],
        [
            "Four-seam grip crosses 4 seams. High spin produces apparent 'rise' and drives whiffs.",
            "95+ mph is solid; 98+ is dominant. Sasaki and Ohtani routinely break 100 mph.",
            "Locating up in the zone uses the apparent-rise effect to boost whiffs (Imanaga's signature).",
            "Recent research on Seam-Shifted Wake explains different movement on visually similar pitches."
        ],
    ),
    make_article(
        "stats-pitch-splitter", "stats", ["statcast", "pitch-type"],
        "スプリット・フィンガー (FS) / フォーク",
        "Splitter (FS) / Forkball",
        "握りを開いて落とす変化球。日本人投手の代名詞的決め球。",
        "Wide-grip pitch that drops sharply. A signature offering for Japanese pitchers.",
        [
            "人差し指と中指を縫い目から離して挟むように握り、回転を抑えて重力で落とす。",
            "4シームと同じ軌道で来て、急激に沈むためバットの上を通過しやすい。Whiff率は40%を超えるケースが多い。",
            "千賀滉大の『お化けフォーク』、今永昇太のスプリッター、佐々木朗希のフォークがMLBで猛威を振るう。",
            "肘への負担が比較的重く、長期使用にはケアが必要。"
        ],
        [
            "Wide split-finger grip suppresses spin so gravity drops the ball.",
            "Looks like a 4-seamer until it dives — whiff rates often exceed 40%.",
            "Senga's 'ghost forkball', Imanaga's splitter, and Sasaki's forkball all dominate in MLB.",
            "Higher elbow load than typical pitches — usage needs careful management."
        ],
    ),
    make_article(
        "stats-pitch-slider-sweeper", "stats", ["statcast", "pitch-type"],
        "スライダー (SL) とスイーパー (ST)",
        "Slider (SL) and Sweeper (ST)",
        "横変化の主力。近年スイーパーは独立した球種として認識された。",
        "Horizontal-movement workhorses. The sweeper recently emerged as a distinct pitch type.",
        [
            "スライダー: カッター寄りの小さな横変化。80年代から定番の決め球。",
            "スイーパー: 大きく横にスライドする現代版。MLB Statcastが2023年から正式に分類。大谷翔平の代名詞。",
            "右投手 vs 右打者で特に有効。ゾーン外への誘い球で空振り量産。",
            "スイーパーは伝統的なスライダーより約3-5インチ多く横変化する。"
        ],
        [
            "Slider: smaller, harder horizontal break (cutter-adjacent). A staple putaway pitch since the '80s.",
            "Sweeper: bigger sweeping break, formally classified by Statcast in 2023. Ohtani's signature.",
            "Especially nasty in same-handed matchups (RHP vs RHH).",
            "Sweepers typically break ~3-5 inches more horizontally than traditional sliders."
        ],
    ),
    make_article(
        "stats-pitch-curveball", "stats", ["statcast", "pitch-type"],
        "カーブ (CU) / ナックルカーブ (KC)",
        "Curveball (CU) / Knuckle-Curve (KC)",
        "縦変化の代表格。回転数2700+rpmで『落とす』のが理想。",
        "The vertical-break standard. Ideally 2700+ RPM for sharp drop.",
        [
            "カーブは前向きの縦変化(=12-6落ち)が基本。山なりの軌道で打者のタイミングを外す緩急球種。",
            "ナックルカーブはナックル握りで指を立て、よりシャープな縦変化を生む。",
            "山本由伸の縦変化系カーブは Statcast で2700+rpm を記録、被打率を低く抑える。",
            "球速差(4シームから-15mph前後)でタイミングを外す効果が大きい。"
        ],
        [
            "Curveball delivers 12-6 vertical break — a slow, looping shape that disrupts timing.",
            "Knuckle-curve grips the index finger like a knuckleball for sharper drop.",
            "Yamamoto's vertical curve hits 2700+ RPM and limits BAA effectively.",
            "The 15+ mph velocity gap from a fastball is critical for the timing-disruption effect."
        ],
    ),
    make_article(
        "stats-pitch-changeup", "stats", ["statcast", "pitch-type"],
        "チェンジアップ (CH)",
        "Changeup (CH)",
        "球速を抑えてタイミングを外す技巧派の決め球。低回転が特徴。",
        "A speed-decreasing pitch that fools timing. Low spin is the hallmark.",
        [
            "チェンジアップは4シームと同じ腕の振りで投げ、握りで球速を10-15mph落とす。",
            "回転数が低いほど沈みやすく、いわゆる『dead ball』効果でバットの下を通る。",
            "サークルチェンジ、Vulcan、フォーク系チェンジなどグリップ多数。",
            "菊池雄星はチェンジアップを使って左打者の対応を改善している。"
        ],
        [
            "Same arm action as a 4-seamer, but the grip drops velocity by 10-15 mph.",
            "Low spin lets the ball drop ('dead ball' effect), passing under the bat.",
            "Variations include circle-change, Vulcan, and split-change.",
            "Yusei Kikuchi has leaned on changeups to attack lefty batters."
        ],
    ),
]


for a in ARTICLES:
    p = OUT / f"{a['slug']}.json"
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generated {len(ARTICLES)} stats articles at {OUT}")
