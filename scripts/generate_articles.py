#!/usr/bin/env python3
"""Generate 40 bilingual article JSON files for SakuraBall."""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "src" / "content" / "articles"
OUT.mkdir(parents=True, exist_ok=True)

ARTICLES = [
    {
        "slug": "ohtani-5hr-pace-2026",
        "date": "2026-04-24", "category": "player", "tags": ["ohtani", "hr-pace"],
        "title_jp": "大谷翔平 5本塁打到達の速さ — 歴代ペース比較",
        "title_en": "Ohtani's Pace to 5 HR: A Historical Look",
        "summary_jp": "シーズン序盤で5号に到達した大谷翔平のペースを、過去の50本塁打達成者の初期ペースと比べて検証する。",
        "summary_en": "Ohtani reached his 5th HR early in the 2026 season. How does this compare with past 50-HR hitters' early pace?",
        "body_jp": [
            "大谷翔平は2026年シーズン序盤で5本塁打に到達した。1試合あたりの本塁打ペースで言えば、過去の50本塁打到達者の平均ペースとほぼ一致する水準だ。",
            "2024年以降の大谷は、打球速度と打球角度の両面で極めて安定している。平均打球速度94.1mph、Barrel率22.1%という数値は、MLB全体でも上位5%に入る。",
            "注目すべきは、5本塁打の内訳が逆方向とプル方向で分かれている点だ。対左右投手ともに対応できるため、シーズン後半にかけて本塁打の伸びが期待できる。",
            "過去の50本塁打打者との比較では、同時期時点の打撃指標が酷似している。xSLGが.500を超えている点も同じで、長期トレンドとしてこのペースは現実的と言える。"
        ],
        "body_en": [
            "Shohei Ohtani hit his 5th home run early in the 2026 season. In per-game pace, this closely matches the average early-season pace of past 50-HR hitters.",
            "Since 2024, Ohtani has been remarkably consistent in both exit velocity and launch angle. A 94.1 mph average exit velocity and 22.1% barrel rate place him in the top 5% of MLB.",
            "What stands out is that his 5 HR are split between opposite-field and pull-side drives. His ability to handle both LHP and RHP suggests further HR growth later in the season.",
            "Compared with past 50-HR hitters at the same point, his batting indicators are strikingly similar. With xSLG above .500, this pace is realistically sustainable."
        ]
    },
    {
        "slug": "imanaga-splitter-2026",
        "date": "2026-04-23", "category": "player", "tags": ["imanaga", "pitch-arsenal"],
        "title_jp": "今永昇太 スプリッター被打率.175の理由",
        "title_en": "Why Imanaga's Splitter Holds Batters to .175",
        "summary_jp": "カブス今永のスプリッターがMLB打者に通用する理由を、空振り率41.9%とHard-Hit率20.0%の観点から分析する。",
        "summary_en": "We dig into why Imanaga's splitter works in MLB — 41.9% whiff rate and a remarkable 20.0% hard-hit rate.",
        "body_jp": [
            "今永昇太のスプリッターは2026年、被打率.175・空振り率41.9%という卓越した数字を残している。MLB平均の空振り率が28%前後であることを考えると、トップクラスの決め球だ。",
            "特筆すべきはHard-Hit率の低さで、わずか20.0%。打者が振りに行ってもバットに当たらず、当たっても打球は上がらない。",
            "要因の一つは4シームとの球速差とトンネル効果だ。4シームと同じ軌道から落ちるため、打者はスイングの判断が遅れる。",
            "シーズン後半にかけて、対左打者の被打率をどこまで抑えられるかが注目点となる。現時点で対右打者には完全に機能している。"
        ],
        "body_en": [
            "Shota Imanaga's splitter has produced elite 2026 numbers: a .175 batting average against and 41.9% whiff rate. With MLB averages near 28%, his splitter ranks near the top.",
            "The hard-hit rate of just 20.0% stands out. Batters either miss entirely, or connect but cannot drive the ball.",
            "A key factor is the velocity gap and tunneling effect with his 4-seam. Because both pitches emerge from the same tunnel, hitters struggle to identify the splitter in time.",
            "The question for the back half of the season is how he fares against lefties. For now, he dominates right-handed batters completely."
        ]
    },
    {
        "slug": "murakami-ops-adjustment",
        "date": "2026-04-22", "category": "player", "tags": ["murakami", "adjustment"],
        "title_jp": "村上宗隆 OPS .992 — MLB適応の軌跡",
        "title_en": "Murakami's .992 OPS and His MLB Adjustment Arc",
        "summary_jp": "ホワイトソックス移籍初年度の村上宗隆が示す高いOPSの内訳を、選球眼とパワー指標から読み解く。",
        "summary_en": "We break down first-year ChiSox slugger Munetaka Murakami's .992 OPS via plate discipline and power indicators.",
        "body_jp": [
            "村上宗隆は移籍初年度の序盤でOPS.992を記録している。出塁率.420はMLB全体でも上位だ。",
            "BB% 19.3%という高い四球率は、NPB時代から磨いた選球眼がMLBでも通用している証明と言える。",
            "一方でK% 32.1%は高めで、特に高めのストレートへの対応に課題が残る。ここは今後の改善余地だ。",
            "xwOBA .433・xSLG .649という期待値指標も極めて高い水準で、出来過ぎではなく実力に裏付けられた数値と言える。"
        ],
        "body_en": [
            "Munetaka Murakami is putting up a .992 OPS early in his MLB debut season. His .420 OBP is among the league leaders.",
            "A 19.3% walk rate demonstrates that the plate discipline he honed in NPB translates directly to MLB.",
            "On the flip side, his 32.1% K rate is high, particularly against high fastballs — a clear area for future improvement.",
            "His .433 xwOBA and .649 xSLG expected metrics are also elite, suggesting the numbers are backed by real quality rather than luck."
        ]
    },
    {
        "slug": "dodgers-vs-cubs-jp-rivalry",
        "date": "2026-04-21", "category": "rivalry", "tags": ["ohtani", "imanaga"],
        "title_jp": "ドジャース対カブス — 日本人選手対決の歴史",
        "title_en": "Dodgers vs. Cubs: History of Japanese Head-to-Heads",
        "summary_jp": "大谷翔平vs今永昇太に代表される日本人対決カードの歴史と、過去の注目試合を振り返る。",
        "summary_en": "From Ohtani vs. Imanaga to past matchups — we revisit Japanese player duels between the Dodgers and Cubs.",
        "body_jp": [
            "ドジャースとカブスの対戦は、日本人選手対決という観点でも注目を集めている。特に大谷翔平と今永昇太の対決は2026年の目玉だ。",
            "過去には前田健太(ドジャース)と他球団の日本人投手対決も話題となり、インターリーグ戦やポストシーズンで複数回実現している。",
            "スタッツ面では、大谷の打撃指標と今永の投手指標が両極端に高いため、1打席ごとの数字がシーズン全体の指標にも影響する。",
            "2026年は両チームが優勝争いに絡むと予想されており、9月以降の直接対決がNL全体の順位にも影響しそうだ。"
        ],
        "body_en": [
            "Dodgers vs. Cubs matchups draw attention for their Japanese-player duels, with Ohtani vs. Imanaga the marquee battle of 2026.",
            "Historically, Kenta Maeda (Dodgers) faced Japanese pitchers on other teams across interleague and postseason games.",
            "Given that Ohtani's batting metrics and Imanaga's pitching metrics are both elite, every plate appearance moves full-season numbers noticeably.",
            "Both teams are expected to contend in 2026, making their September head-to-heads potentially decisive for the NL standings."
        ]
    },
    {
        "slug": "statcast-101-barrel",
        "date": "2026-04-20", "category": "statcast", "tags": ["statcast", "barrel"],
        "title_jp": "Statcast入門: Barrel率とは何か",
        "title_en": "Statcast 101: What Is Barrel Rate?",
        "summary_jp": "Barrelの定義、計算基準、なぜ打球速度と打球角度の組み合わせが重要なのかを解説する。",
        "summary_en": "We explain what a Barrel is, how it's calculated, and why the combination of exit velocity and launch angle matters.",
        "body_jp": [
            "Barrelとは、打球速度と打球角度の組み合わせが、打率.500・長打率1.500以上を生む条件を満たした打球のことだ。",
            "具体的には打球速度98mph以上、打球角度26-30度が基本となり、打球速度が上がるほど許容される打球角度の幅も広がる。",
            "Barrel率が高い打者は、本塁打や長打を量産する可能性が高い。大谷翔平の22.1%はMLBトップクラスだ。",
            "ただしBarrel率だけでは評価できない部分もあり、Contact率や選球眼と併せて見る必要がある。"
        ],
        "body_en": [
            "A Barrel is a batted ball whose combination of exit velocity and launch angle produces at least a .500 AVG and 1.500 SLG historically.",
            "The baseline is 98+ mph exit velocity at 26-30° launch angle, with the angle range widening as velocity increases.",
            "Hitters with high barrel rates tend to generate HRs and extra-base hits. Ohtani's 22.1% rate is elite in MLB.",
            "That said, barrel rate alone doesn't tell the full story — it should be read alongside contact rate and plate discipline."
        ]
    },
    {
        "slug": "statcast-101-xwoba",
        "date": "2026-04-19", "category": "statcast", "tags": ["statcast", "xwoba"],
        "title_jp": "Statcast入門: xwOBAとwOBAの違い",
        "title_en": "Statcast 101: xwOBA vs. wOBA",
        "summary_jp": "運の要素を除いた期待値指標としてのxwOBAと、実績指標のwOBAをどう使い分けるかを整理する。",
        "summary_en": "We clarify when to use xwOBA (expected, luck-neutral) versus wOBA (actual outcomes).",
        "body_jp": [
            "wOBAはOn-Base Percentageを進化させた総合打撃指標で、各種打撃イベントを加重して算出される。",
            "xwOBAは、打球の打球速度・打球角度・走力から期待値を算出した指標で、実績ではなく「内容」を評価する。",
            "xwOBA > wOBAなら不運、xwOBA < wOBAなら幸運と解釈できる。サンプルサイズが大きいほど両者は収束する。",
            "村上宗隆の2026年序盤はxwOBA.433と極めて高く、この調子が続けばOPSはさらに伸びる可能性がある。"
        ],
        "body_en": [
            "wOBA is a rate stat that weights each offensive event (walk, single, HR, etc.) and improves on OBP.",
            "xwOBA uses exit velocity, launch angle, and sprint speed to produce an expected, luck-neutral version of the same metric.",
            "If xwOBA > wOBA, a hitter has been unlucky; xwOBA < wOBA means lucky. Over larger samples the two tend to converge.",
            "Murakami's early-2026 xwOBA of .433 is elite — if this pace holds, his OPS has room to climb further."
        ]
    },
    {
        "slug": "statcast-101-ev-la",
        "date": "2026-04-18", "category": "statcast", "tags": ["statcast", "exit-velocity"],
        "title_jp": "Statcast入門: 打球速度と打球角度の黄金比",
        "title_en": "Statcast 101: The Golden Ratio of EV and Launch Angle",
        "summary_jp": "長打を生みやすい打球速度と打球角度の組み合わせを、ヒートマップから読み解く。",
        "summary_en": "We use heatmaps to understand which combinations of exit velocity and launch angle drive extra-base hits.",
        "body_jp": [
            "MLBの過去データでは、打球速度95mph以上・打球角度15-35度の組み合わせが長打の最大確率ゾーンだ。",
            "打球角度が低すぎるとゴロ、高すぎるとポップアップになりやすい。打球速度が低いと平均的な長打でも届かない。",
            "大谷翔平の平均打球速度94.1mph・平均打球角度12.6度は、長打ゾーンの入口に位置している。",
            "村上宗隆の平均打球速度96.0mph・平均打球角度16.5度はほぼ黄金比の中心にあり、長打量産の裏付けとなっている。"
        ],
        "body_en": [
            "Historically, MLB batted balls hit 95+ mph at 15-35° launch angle produce the highest extra-base hit probability.",
            "Too low a launch angle yields grounders; too high becomes pop-ups. Low exit velocity limits even well-struck balls.",
            "Ohtani's averages (94.1 mph EV, 12.6° LA) sit at the entrance of the XBH zone.",
            "Murakami's averages (96.0 mph EV, 16.5° LA) land near the center of the golden zone, underpinning his XBH production."
        ]
    },
    {
        "slug": "ohtani-pitcher-return-2026",
        "date": "2026-04-17", "category": "player", "tags": ["ohtani", "pitching"],
        "title_jp": "大谷翔平 2026年投手復帰 初登板レビュー",
        "title_en": "Ohtani's 2026 Pitching Return: Debut Start Review",
        "summary_jp": "トミージョン手術後の復帰登板で見せた球速・球種と、ERA 0.38の現時点での評価。",
        "summary_en": "Ohtani's post-Tommy John return: velocity, pitch mix, and an early-season 0.38 ERA.",
        "body_jp": [
            "大谷翔平は2026年、ドジャースで投手として復帰した。初登板では4シームの平均球速が手術前とほぼ同じ水準まで戻った。",
            "現時点での成績はERA 0.38・WHIP 0.85と突出している。2勝0敗、奪三振15という数字も試合数を考えれば極めて高い効率だ。",
            "球種使用率は4シーム44.4%が中心で、スプリッターとスイーパーを織り交ぜる従来のスタイルを維持している。",
            "打撃との両立負荷はあるが、登板間隔を5日空けることでコンディションを管理している。"
        ],
        "body_en": [
            "Ohtani returned to pitching for the Dodgers in 2026. In his debut start, his 4-seam velocity nearly matched pre-surgery levels.",
            "Early results: 0.38 ERA, 0.85 WHIP. His 2-0 record with 15 strikeouts marks elite efficiency given the small sample.",
            "His arsenal is 4-seam-led at 44.4%, mixed with splitters and sweepers — the same profile as before.",
            "Managing the two-way workload means 5-day spacing between starts to preserve condition."
        ]
    },
    {
        "slug": "imanaga-command-zone",
        "date": "2026-04-16", "category": "player", "tags": ["imanaga", "command"],
        "title_jp": "今永の制球力 — ゾーン内投球率でみる",
        "title_en": "Imanaga's Command: A Zone% Perspective",
        "summary_jp": "今永のゾーン内投球率と、それを支える投球フォームの特徴を整理する。",
        "summary_en": "We examine Imanaga's Zone% and the mechanical traits that enable it.",
        "body_jp": [
            "今永昇太のゾーン内投球率はMLB平均を上回る。ストライクゾーンに投げ込む能力が、MLB打者相手にも通用している。",
            "特徴は低いリリースポイントから浮き上がるように見える4シームで、打者からは実際の球速以上に速く感じられる。",
            "ゾーン内に投げ込みつつ長打を打たれない理由は、ゾーン内での投球の質と変化球のシグナルが分かりにくい点にある。",
            "シーズン通してこの制球を維持できれば、WHIPも1.00台に収束する可能性が高い。"
        ],
        "body_en": [
            "Imanaga's Zone% sits above the MLB average. His ability to challenge the strike zone translates cleanly to MLB.",
            "His signature is a 4-seam that appears to rise out of a low release slot, making it feel faster than its radar reading.",
            "He avoids hard contact in the zone thanks to pitch quality and disguised offspeed signals.",
            "If he holds this command all season, his WHIP should settle near 1.00."
        ]
    },
    {
        "slug": "murakami-pull-power",
        "date": "2026-04-15", "category": "player", "tags": ["murakami", "pull"],
        "title_jp": "村上の長打力 — Pull%で見る打球方向",
        "title_en": "Murakami's Power: A Pull% Breakdown",
        "summary_jp": "村上宗隆のプル方向への打球割合と、長打力との相関を検証する。",
        "summary_en": "We check the correlation between Murakami's pull direction frequency and his power output.",
        "body_jp": [
            "村上宗隆の長打は多くがプル方向(右方向)に集中している。本塁打10本のうち大多数が右翼スタンドだ。",
            "Pull%が高い左打者は相手シフトの影響を受けやすかったが、2023年のシフト禁止後はプル打者の利点が増した。",
            "MLB球場の多くは右中間から右翼が狭めで、村上のような引っ張り型にとって有利な球場が複数存在する。",
            "今後は逆方向への長打が増えるかどうかが、本塁打40本ペースを維持できるかの鍵となる。"
        ],
        "body_en": [
            "Most of Murakami's extra-base hits cluster to the pull side — the large majority of his 10 HRs have cleared the right-field fence.",
            "High-Pull% LHHs historically suffered from the shift, but the 2023 shift ban flipped this into an advantage.",
            "Many MLB parks play small in right-center and right field, favoring pull hitters like Murakami.",
            "Whether he starts driving balls the other way will decide if he can hold a 40-HR pace."
        ]
    },
    {
        "slug": "nomo-pioneer-legacy",
        "date": "2026-04-14", "category": "history", "tags": ["history", "nomo"],
        "title_jp": "野茂英雄から始まった日本人MLB挑戦史",
        "title_en": "The Japanese MLB Legacy Started by Hideo Nomo",
        "summary_jp": "1995年の野茂英雄によるMLB挑戦が、日本人選手にとってどのような扉を開いたかを整理する。",
        "summary_en": "How Hideo Nomo's 1995 MLB leap opened the door for Japanese players that followed.",
        "body_jp": [
            "1995年、野茂英雄がドジャースで最多奪三振のタイトルを獲得した。これが日本人選手MLB挑戦の第一歩となった。",
            "それまでは日米間の契約制度が整っておらず、日本人選手がMLBでプレーすることは事実上困難だった。",
            "野茂の成功を受けてポスティングシステムが整備され、2000年以降は多くの日本人投手がMLBに挑戦するようになった。",
            "イチロー、松井秀喜、ダルビッシュ、大谷翔平まで続く系譜は、すべて野茂の挑戦から始まった。"
        ],
        "body_en": [
            "In 1995, Hideo Nomo led the NL in strikeouts with the Dodgers — the first real breakthrough for Japanese players in MLB.",
            "Before that, inter-league contract rules made it practically impossible for Japanese players to come over.",
            "Nomo's success accelerated the creation of the posting system, and from 2000 onward many Japanese pitchers followed.",
            "The lineage from Nomo to Ichiro, Matsui, Darvish, and now Ohtani traces back to that single act of courage."
        ]
    },
    {
        "slug": "ichiro-batting-average-legacy",
        "date": "2026-04-13", "category": "history", "tags": ["history", "ichiro"],
        "title_jp": "イチロー 打率3割の年数とMLB史での位置づけ",
        "title_en": "Ichiro's Run of .300 Seasons and His MLB Standing",
        "summary_jp": "イチローがMLBで記録した10年連続3割・200安打と、その歴史的評価を振り返る。",
        "summary_en": "A look back at Ichiro's 10 consecutive .300/200-hit seasons and his historical standing.",
        "body_jp": [
            "イチローは2001-2010年、10年連続で打率3割かつ200安打を記録した。これはMLB史上初の記録だ。",
            "シーズン最多安打記録262本(2004年)も、現在まで破られていない。",
            "守備面でもゴールドグラブ賞を10回受賞するなど、走攻守の総合力で評価された。",
            "MLB通算3089安打、日米通算4367安打という数字は、野手としての歴史的位置づけを揺るぎないものにしている。"
        ],
        "body_en": [
            "Ichiro hit .300+ with 200+ hits in 10 straight seasons from 2001 to 2010 — the first player in MLB history to do so.",
            "His 262-hit single-season record (2004) still stands today.",
            "He also won 10 Gold Gloves, earning elite status on defense to go with his bat and legs.",
            "His 3,089 MLB hits and 4,367 career hits (combined NPB+MLB) cement his historical place as an all-time great."
        ]
    },
    {
        "slug": "matsui-yankees-rbi",
        "date": "2026-04-12", "category": "history", "tags": ["history", "matsui"],
        "title_jp": "松井秀喜 ヤンキース時代の打点王",
        "title_en": "Hideki Matsui: RBI Leader with the Yankees",
        "summary_jp": "松井秀喜がヤンキースで残した打点と、2009年ワールドシリーズMVPに至るキャリアを振り返る。",
        "summary_en": "We revisit Matsui's Yankees RBI production, culminating in his 2009 World Series MVP.",
        "body_jp": [
            "松井秀喜は2003年にヤンキースに入団し、初年度から106打点を記録。勝負強さが高く評価された。",
            "2009年ワールドシリーズではMVPに選出され、6試合で打率.615・3本塁打・8打点の爆発を見せた。",
            "通算MLB成績は175本塁打・760打点。ポストシーズンでの活躍も含めれば、勝負どころに強い打者として記憶されている。",
            "NPB通算332本塁打と合わせると、日米通算で500本塁打を超える長距離砲としての功績を残した。"
        ],
        "body_en": [
            "Hideki Matsui joined the Yankees in 2003 and drove in 106 runs in his rookie MLB year, earning a reputation for clutch production.",
            "He was named 2009 World Series MVP after hitting .615 with 3 HRs and 8 RBIs in six games.",
            "His MLB career totals: 175 HRs and 760 RBIs. Including postseason impact, he is remembered as a clutch hitter.",
            "Adding his 332 NPB HRs gives him more than 500 combined career home runs across both leagues."
        ]
    },
    {
        "slug": "darvish-strikeouts-1900",
        "date": "2026-04-11", "category": "history", "tags": ["history", "darvish"],
        "title_jp": "ダルビッシュ有 通算1900奪三振への歩み",
        "title_en": "Yu Darvish's Path to 1,900 MLB Strikeouts",
        "summary_jp": "日本人投手MLB通算奪三振記録を更新し続けるダルビッシュ有のキャリア軌跡。",
        "summary_en": "Tracing Yu Darvish's career as he continues to break the Japanese MLB strikeout record.",
        "body_jp": [
            "ダルビッシュ有は2012年にレンジャーズ入団、現在はパドレスでプレーしている。日本人投手MLB通算奪三振記録を更新中だ。",
            "球種の多さが特徴で、4シーム、カッター、スライダー、スプリット、カーブなど10種類以上を使い分ける。",
            "40代目前になってもシーズン150奪三振以上を記録しており、長期キャリアの模範と言える。",
            "2025年には通算1900奪三振を達成、日本人投手として唯一2000奪三振が現実的な射程に入っている。"
        ],
        "body_en": [
            "Yu Darvish joined the Rangers in 2012 and now pitches for the Padres — he currently holds the MLB strikeout record among Japanese pitchers and keeps extending it.",
            "His pitch variety is unrivaled: 4-seam, cutter, slider, splitter, curve and more — 10+ distinct offerings.",
            "Nearing 40, he still posts 150+ strikeouts a year, modeling long-career durability.",
            "He surpassed 1,900 career MLB strikeouts in 2025 — the only Japanese pitcher with 2,000 in realistic reach."
        ]
    },
    {
        "slug": "tanaka-mlb-career-recap",
        "date": "2026-04-10", "category": "history", "tags": ["history", "tanaka"],
        "title_jp": "田中将大 NPB復帰までのMLBキャリア総括",
        "title_en": "Masahiro Tanaka's MLB Career: A Retrospective",
        "summary_jp": "ヤンキースでの7年間とNPB復帰後までを含めた、田中将大の投手人生を振り返る。",
        "summary_en": "We summarize Masahiro Tanaka's seven Yankees years and his path back to NPB.",
        "body_jp": [
            "田中将大は2014年にヤンキース入団。初年度から13勝をあげ、最優秀新人候補にも名を連ねた。",
            "通算MLB成績は78勝46敗・防御率3.74。特にスプリッターによる奪三振が印象的だった。",
            "2021年にNPB楽天に復帰。MLBキャリアで培った配球と制球が日本球界でも通用した。",
            "ポストシーズンでの好投も目立ち、ヤンキース先発として重要な役割を担った時期があった。"
        ],
        "body_en": [
            "Masahiro Tanaka joined the Yankees in 2014 and went 13-5 as a rookie, earning Rookie of the Year consideration.",
            "His career MLB line: 78-46, 3.74 ERA. His splitter was especially memorable as a strikeout pitch.",
            "He returned to NPB Rakuten in 2021, applying the command and pitch sequencing he developed in MLB.",
            "His postseason performances were notable, and he was a key Yankees starter during a competitive stretch."
        ]
    },
    {
        "slug": "kikuchi-rotation-to-pen",
        "date": "2026-04-09", "category": "player", "tags": ["kikuchi", "role-change"],
        "title_jp": "菊池雄星 先発→中継ぎ転向の成功例",
        "title_en": "Yusei Kikuchi: A Successful Starter-to-Reliever Move",
        "summary_jp": "先発から中継ぎに転向した菊池雄星の球速上昇と奪三振率改善をまとめる。",
        "summary_en": "We look at Kikuchi's velocity bump and strikeout-rate improvement after moving to the bullpen.",
        "body_jp": [
            "菊池雄星は近年、先発から中継ぎへの役割転換を試みている。1イニング集中型の投球で球速が1-2mph向上した。",
            "中継ぎ転向後の奪三振率(K/9)は11を超える水準で、先発時代の8台から大幅に改善している。",
            "左のリリーバーはMLBで需要が高く、役割転換は価値向上にも直結する。",
            "今後フル転向するか、先発にも対応するスイングマン型でいくかが注目される。"
        ],
        "body_en": [
            "Yusei Kikuchi has been experimenting with a starter-to-reliever move recently. Focused one-inning outings lifted his velocity by 1-2 mph.",
            "Post-move, his K/9 sits above 11 — a sharp improvement from the 8s he posted as a starter.",
            "Left-handed relievers are in strong demand in MLB, and a role change directly improves his market value.",
            "The open question is whether he commits fully to the bullpen or lands as a swingman."
        ]
    },
    {
        "slug": "maeda-dodgers-vs-twins",
        "date": "2026-04-08", "category": "history", "tags": ["history", "maeda"],
        "title_jp": "前田健太 ドジャース→ツインズ時代の比較",
        "title_en": "Kenta Maeda: Dodgers Era vs. Twins Era",
        "summary_jp": "前田健太がドジャース時代とツインズ時代で見せた投球内容の違いを整理する。",
        "summary_en": "We compare Kenta Maeda's pitching profile between his Dodgers and Twins tenures.",
        "body_jp": [
            "前田健太はドジャース時代はスライダーを軸にした抑え型の先発として起用された。",
            "ツインズ移籍後は先発中心の役割となり、2020年にはサイ・ヤング賞投票2位まで上り詰めた。",
            "スライダーの被打率は両時代を通じて非常に低く、MLBでも屈指のピッチとして評価された。",
            "手術による離脱も経験したが、復帰後も高い奪三振率を維持している。"
        ],
        "body_en": [
            "With the Dodgers, Maeda served as a slider-first starter with bullpen-style deployment.",
            "After moving to the Twins, he settled into a full starter role and finished 2nd in 2020 AL Cy Young voting.",
            "Across both eras, his slider's batting average against was extremely low — an elite offering by MLB standards.",
            "Despite surgery and time off, he returned with his strikeout rates intact."
        ]
    },
    {
        "slug": "suzuki-cubs-middle-order",
        "date": "2026-04-07", "category": "player", "tags": ["suzuki", "cubs"],
        "title_jp": "鈴木誠也 カブス打線の中軸として",
        "title_en": "Seiya Suzuki: Heart of the Cubs Order",
        "summary_jp": "鈴木誠也がカブス打線で果たす役割と、シーズンごとの成績推移を振り返る。",
        "summary_en": "Suzuki's role in the Cubs lineup and his season-to-season trend.",
        "body_jp": [
            "鈴木誠也は2022年にカブス入団。以降、打線の中軸として定着している。",
            "課題だったストレート対応も改善傾向にあり、OPS.800台を維持している。",
            "Hard-Hit率はリーグ平均を上回り、Barrel率も高水準だ。",
            "今永昇太との日本人バッテリー的な並びも、カブスファンには大きな話題となっている。"
        ],
        "body_en": [
            "Seiya Suzuki joined the Cubs in 2022 and has been a fixture in the middle of the order since.",
            "His fastball handling, once a concern, has steadily improved — and he has held an .800+ OPS.",
            "His hard-hit rate sits above league average, and his barrel rate is strong.",
            "Pairing him with Imanaga gives Cubs fans a true Japanese-duo centerpiece."
        ]
    },
    {
        "slug": "yoshida-redsox-contract",
        "date": "2026-04-06", "category": "player", "tags": ["yoshida", "contract"],
        "title_jp": "吉田正尚 レッドソックス契約の評価",
        "title_en": "Evaluating Masataka Yoshida's Red Sox Contract",
        "summary_jp": "5年9000万ドルでレッドソックス入りした吉田正尚の契約評価を成績から再検討する。",
        "summary_en": "We revisit the 5-year, $90M Yoshida deal with Boston in light of his on-field output.",
        "body_jp": [
            "吉田正尚は2023年に5年9000万ドルでレッドソックスに入団した。コンタクト能力に定評があった。",
            "初年度は打率.289・15本塁打と期待通りのスタートを切ったが、2年目以降は怪我の影響もあり成績が伸び悩んでいる。",
            "K%が低い打者としてMLB全体でも上位だが、長打力への期待値は契約規模に見合っていない可能性がある。",
            "2026年シーズンは契約中盤。ここでどこまで戻せるかが将来評価を左右する。"
        ],
        "body_en": [
            "Yoshida signed a 5-year, $90M deal with Boston in 2023, arriving with an elite contact reputation.",
            "Year 1 went well (.289, 15 HRs), but years 2+ were limited by injury and uneven output.",
            "His K% ranks among the lowest in MLB, though his power output may not match his contract tier.",
            "2026 is the middle of his deal — how much he rebounds will shape the contract's legacy."
        ]
    },
    {
        "slug": "fujinami-orioles-revival",
        "date": "2026-04-05", "category": "player", "tags": ["fujinami", "orioles"],
        "title_jp": "藤浪晋太郎 オリオールズでの復活",
        "title_en": "Shintaro Fujinami's Revival with the Orioles",
        "summary_jp": "制球難を克服しつつある藤浪晋太郎のMLBでの現状と、役割の変化を整理する。",
        "summary_en": "Fujinami has been taming his control issues. We look at his current MLB status and role shifts.",
        "body_jp": [
            "藤浪晋太郎は制球難を抱えながらもMLBでプレーを続けている。160km/hを超える球速は変わらず魅力的だ。",
            "中継ぎとしての起用が中心で、短いイニングに集中することで制球が安定してきた。",
            "奪三振率は高く、好調時は1イニング2奪三振ペースで投げる。",
            "MLB全体で高速球の需要は高いため、ロースターに残り続けられる可能性は十分にある。"
        ],
        "body_en": [
            "Shintaro Fujinami continues in MLB despite ongoing control issues. His triple-digit velocity remains a compelling asset.",
            "He's used mostly out of the bullpen, where shorter outings have helped stabilize his command.",
            "His strikeout rate is high — in good stretches he K's roughly 2 per inning.",
            "With MLB's demand for elite velocity, he has a strong chance of holding a roster spot."
        ]
    },
    {
        "slug": "senga-ghost-forkball",
        "date": "2026-04-04", "category": "player", "tags": ["senga", "forkball"],
        "title_jp": "千賀滉大 メッツ時代の\"お化けフォーク\"",
        "title_en": "Kodai Senga's Ghost Forkball with the Mets",
        "summary_jp": "千賀滉大の代名詞であるお化けフォークの落差と、MLB打者への通用性を確認する。",
        "summary_en": "A look at Senga's signature ghost forkball, its drop profile, and how it plays vs. MLB hitters.",
        "body_jp": [
            "千賀滉大の\"お化けフォーク\"は、MLBでも屈指の落差を持つ球として評価されている。",
            "平均縦変化量はスプリット系統でも上位クラスで、打者からは\"消えるように見える\"と証言された。",
            "被打率.150以下、空振り率40%以上を記録した時期もあり、メッツのローテーションで中心的な役割を果たした。",
            "怪我による離脱もあったが、復帰後もこの球は健在で、今後も武器として機能すると見られる。"
        ],
        "body_en": [
            "Kodai Senga's ghost forkball is among the most extreme drop pitches in MLB.",
            "Its vertical drop is elite in the splitter family, and hitters have described it as 'disappearing' on them.",
            "In strong stretches, it yielded a BA under .150 and a 40%+ whiff rate, anchoring him in the Mets rotation.",
            "Despite injury-related absences, the pitch has returned intact and projects to remain his primary weapon."
        ]
    },
    {
        "slug": "yamamoto-325m-contract",
        "date": "2026-04-03", "category": "player", "tags": ["yamamoto", "contract"],
        "title_jp": "山本由伸 12年3億2500万ドル契約の妥当性",
        "title_en": "Is Yamamoto's 12-Year, $325M Deal Worth It?",
        "summary_jp": "NPB最優秀防御率3年連続の山本由伸とドジャースの超大型契約を、現状の成績で再評価する。",
        "summary_en": "We re-evaluate Yamamoto's massive Dodgers deal in light of his on-field production so far.",
        "body_jp": [
            "山本由伸は2024年にドジャースと12年3億2500万ドルで契約した。日本人投手として史上最大規模だ。",
            "初年度は怪我による離脱もあったが、復帰後の成績は防御率3点台前半で推移している。",
            "NPB時代から続くストレートとフォーク・スプリットの組み合わせはMLBでも機能している。",
            "契約長さゆえにリスクはあるが、エース級の数字を数シーズン残せば十分に元が取れる試算もある。"
        ],
        "body_en": [
            "Yamamoto signed a 12-year, $325M deal with the Dodgers in 2024 — the largest ever for a Japanese pitcher.",
            "Year 1 included time missed due to injury, but post-return he has hovered around a low-3 ERA.",
            "His NPB-era fastball-splitter combo translates to MLB effectively.",
            "The contract length carries risk, but several ace-caliber seasons would make it pay off per many projections."
        ]
    },
    {
        "slug": "matsui-yuki-padres",
        "date": "2026-04-02", "category": "player", "tags": ["matsui-yuki", "padres"],
        "title_jp": "松井裕樹 パドレス移籍の影響",
        "title_en": "Yuki Matsui's Move to the Padres",
        "summary_jp": "NPBのクローザーとして活躍した松井裕樹のMLBセットアッパー役について見る。",
        "summary_en": "We examine former NPB closer Yuki Matsui's new role as an MLB setup man.",
        "body_jp": [
            "松井裕樹はNPBでセーブ王を複数回獲得し、MLBでのクローザー候補として期待された。",
            "パドレスでは主にセットアッパー的な役割で起用され、左打者対策の重要な役割を担っている。",
            "奪三振能力は健在で、スライダーとチェンジアップの組み合わせがMLB打者にも通用している。",
            "シーズン終盤には9回の重要場面で起用される可能性もあり、役割拡大が注目される。"
        ],
        "body_en": [
            "Yuki Matsui led NPB in saves multiple times and arrived as a projected MLB closer candidate.",
            "With San Diego he's been used mainly as a setup man, especially in LHH matchups.",
            "His strikeout ability is intact — the slider-changeup combo works on MLB hitters too.",
            "Late-season 9th-inning opportunities are plausible, and any role expansion will be worth watching."
        ]
    },
    {
        "slug": "uwasawa-debut-struggles",
        "date": "2026-04-01", "category": "player", "tags": ["uwasawa", "rookie"],
        "title_jp": "上沢直之 MLB初年度の苦戦と今後",
        "title_en": "Naoyuki Uwasawa: Rookie Year Struggles and Outlook",
        "summary_jp": "日本ハムからMLB移籍した上沢直之の初年度データをもとに、今後の適応可能性を探る。",
        "summary_en": "Using his rookie data, we consider whether Uwasawa can adapt going forward.",
        "body_jp": [
            "上沢直之は2024年に日本ハムからMLBに移籍したが、初年度は苦戦した。球速面での絶対的な優位性がない点が主因とされる。",
            "変化球の質は悪くないものの、MLB打者のコンタクト能力の高さに対して球種の比率を再構築する必要がある。",
            "マイナー経由での再挑戦も行われており、適応次第ではメジャー定着も十分に可能だ。",
            "2026年にどこまで戻せるかが、MLBキャリア継続の鍵となる。"
        ],
        "body_en": [
            "Uwasawa moved from Nippon-Ham to MLB in 2024 and struggled early, in part because he lacks a true velocity advantage.",
            "His breaking ball quality isn't bad, but his mix needs reshaping against MLB hitters' elite contact skills.",
            "He has retried via the minors — with the right adjustments, sticking in the majors remains realistic.",
            "2026 is likely the pivotal year for his continued MLB career."
        ]
    },
    {
        "slug": "breakout-candidates-minor",
        "date": "2026-03-31", "category": "prospects", "tags": ["prospects", "minor"],
        "title_jp": "今季ブレイク候補 — マイナー注目株",
        "title_en": "Breakout Candidates: Minor League Names to Watch",
        "summary_jp": "2026年シーズン中にメジャー昇格が期待される日本人マイナー選手を紹介する。",
        "summary_en": "A quick look at Japanese minor leaguers who could be called up during 2026.",
        "body_jp": [
            "各球団のマイナーには、日本出身の選手が複数在籍している。2026年内の昇格候補として注目される名前もある。",
            "投手ではNPB出身で中継ぎ適性を評価された選手が、3A昇格後に速球の質を上げている例がある。",
            "野手では韓国・台湾経由でのMLB挑戦ではなく、日本の社会人・独立リーグ出身者も門戸が開かれつつある。",
            "昇格のタイミングは怪我人の発生やトレードによる玉突きが大きく影響するため、ニュースは随時チェックしたい。"
        ],
        "body_en": [
            "Several Japanese-born players are on MLB organizations' minor league rosters, with a few potential 2026 call-ups.",
            "On the pitching side, some NPB-background relievers have ticked up their fastball quality after reaching Triple-A.",
            "Position-player doors are now opening to players from Japan's industrial and independent leagues too.",
            "Promotions tend to hinge on injuries and trade knock-ons, so staying current with news is essential."
        ]
    },
    {
        "slug": "nl-west-2026-preview",
        "date": "2026-03-30", "category": "team", "tags": ["team", "nl-west"],
        "title_jp": "2026シーズン NL西地区展望",
        "title_en": "2026 NL West Preview",
        "summary_jp": "ドジャース・パドレスを中心に、2026年NL西地区の順位予想と注目ポイントをまとめる。",
        "summary_en": "A Dodgers/Padres-centered preview of the 2026 NL West, with standings projections and key storylines.",
        "body_jp": [
            "2026年のNL西地区は、ドジャースとパドレスの2強を中心に展開する見込みだ。",
            "ドジャースには大谷翔平・山本由伸が、パドレスにはダルビッシュ有・松井裕樹がおり、日本人選手の存在感も大きい。",
            "ジャイアンツとダイヤモンドバックスの追い上げ次第では、Wild Card争いも激化しそうだ。",
            "シーズン終盤の直接対決日程が、順位を決める上で重要な節目となる。"
        ],
        "body_en": [
            "The 2026 NL West is likely to be a two-horse race between the Dodgers and Padres.",
            "The Dodgers feature Ohtani and Yamamoto; the Padres have Darvish and Matsui — a strong Japanese presence on both sides.",
            "If the Giants and Diamondbacks push, the Wild Card race should heat up further.",
            "Late-season head-to-heads will be the pivotal standings moments."
        ]
    },
    {
        "slug": "al-east-2026-preview",
        "date": "2026-03-29", "category": "team", "tags": ["team", "al-east"],
        "title_jp": "2026シーズン AL東地区展望",
        "title_en": "2026 AL East Preview",
        "summary_jp": "ヤンキース・オリオールズ・レッドソックスの3強を中心に、AL東地区の展望をまとめる。",
        "summary_en": "A preview of the AL East, centered on the Yankees, Orioles, and Red Sox as the likely top trio.",
        "body_jp": [
            "2026年AL東地区は、ヤンキース・オリオールズ・レッドソックスの3チームによる優勝争いが予想される。",
            "日本人選手では吉田正尚(レッドソックス)、藤浪晋太郎(オリオールズ)が在籍する。",
            "レイズとブルージェイズはやや戦力的に劣るが、若手の台頭次第では中位進出の可能性は残る。",
            "伝統的に接戦の多い地区で、勝率5割周辺で3-4チームが競る展開が濃厚だ。"
        ],
        "body_en": [
            "The 2026 AL East should be a three-way race among the Yankees, Orioles, and Red Sox.",
            "Japanese-born players in the division include Yoshida (Red Sox) and Fujinami (Orioles).",
            "The Rays and Blue Jays trail slightly on paper, but young talent could push them into the middle tier.",
            "In a traditionally tight division, three to four teams near .500 is the most likely shape."
        ]
    },
    {
        "slug": "pitch-clock-impact",
        "date": "2026-03-28", "category": "rules", "tags": ["rules", "pitch-clock"],
        "title_jp": "MLB新ルール: ピッチクロックの影響",
        "title_en": "MLB Rule Change: Pitch Clock's Impact",
        "summary_jp": "2023年導入のピッチクロックがもたらした試合時間短縮と、選手のリズムへの影響を整理する。",
        "summary_en": "We examine game-length reductions and rhythm effects from the 2023 pitch-clock rules.",
        "body_jp": [
            "2023年に導入されたピッチクロックは、MLBの平均試合時間を30分以上短縮した。",
            "日本人投手には、NPB時代からテンポの良い投手が多く、ピッチクロックへの適応は比較的スムーズだったと言える。",
            "一方で、打者への影響は大きく、打席でのタイミング調整に苦労する選手も見られる。",
            "リズムが変わった結果、盗塁数の増加や四球率の変動など副次的な影響も生じている。"
        ],
        "body_en": [
            "The pitch clock introduced in 2023 cut average MLB game times by more than 30 minutes.",
            "Many Japanese pitchers were already tempo-driven from their NPB days, so adaptation has been relatively smooth.",
            "For hitters, the effect has been larger — some have struggled to manage timing within the box.",
            "Secondary effects include higher stolen base totals and shifts in walk rates."
        ]
    },
    {
        "slug": "base-size-stolen-base",
        "date": "2026-03-27", "category": "rules", "tags": ["rules", "stolen-base"],
        "title_jp": "ベースサイズ拡大が盗塁数に与えた影響",
        "title_en": "Larger Bases and the Stolen-Base Boom",
        "summary_jp": "2023年のベースサイズ拡大後、盗塁成功率と盗塁数がどう変化したかをデータで追う。",
        "summary_en": "We track how stolen base totals and success rates shifted after the 2023 base-size change.",
        "body_jp": [
            "2023年、MLBはベースサイズを15インチから18インチに拡大した。塁間の実効距離が短くなり、盗塁成功率が向上した。",
            "リーグ全体の盗塁数は翌年以降、前年比2-3割増加している。",
            "日本人選手の中でも走力のある選手は恩恵を受け、シーズン盗塁数を伸ばすケースが増えた。",
            "大谷翔平のように長打と盗塁の両方で数字を残すタイプは、40-40到達の再現性が高まっている。"
        ],
        "body_en": [
            "MLB enlarged bases from 15 to 18 inches in 2023, shortening effective base paths and lifting SB success rates.",
            "League-wide stolen bases have increased 20-30% year-over-year since.",
            "Faster Japanese players have benefited, with some posting career-high SB totals.",
            "Power-speed players like Ohtani now have improved odds of repeating 40-40 seasons."
        ]
    },
    {
        "slug": "shift-ban-lhh-trends",
        "date": "2026-03-26", "category": "rules", "tags": ["rules", "shift"],
        "title_jp": "シフト禁止後の左打者成績トレンド",
        "title_en": "Left-Handed Hitter Trends Since the Shift Ban",
        "summary_jp": "2023年のシフト制限以降、左打者の打率とBABIPがどう変化しているかを分析する。",
        "summary_en": "We analyze how LHH batting average and BABIP have shifted since the 2023 shift restrictions.",
        "body_jp": [
            "2023年にMLBは極端な守備シフトを制限した。特に左打者のBABIPが平均で.010程度上昇している。",
            "この変化は村上宗隆のようなプル型左打者に恩恵をもたらしている。",
            "一方、シフト対策として逆方向打法を磨いてきた選手は、変化への再適応を求められている。",
            "投手側ではゴロを打たせる投球の価値が若干変わり、配球の見直しが進んでいる。"
        ],
        "body_en": [
            "MLB restricted extreme defensive shifts in 2023, and LHH BABIP has risen roughly .010 on average.",
            "This change has helped pull-heavy LHHs like Murakami.",
            "Meanwhile, hitters who had trained to hit the other way against shifts are now re-adjusting.",
            "On the pitching side, the value of ground-ball induction has shifted slightly, prompting pitch-mix changes."
        ]
    },
    {
        "slug": "jp-pitchers-contact-culture",
        "date": "2026-03-25", "category": "culture", "tags": ["culture", "pitching"],
        "title_jp": "日本人投手 vs MLBのコンタクト文化",
        "title_en": "Japanese Pitchers Meet MLB's Contact Culture",
        "summary_jp": "球数制限や打席での粘りなど、MLBのコンタクト重視の文化と日本人投手の戦い方を考察する。",
        "summary_en": "We look at how Japanese pitchers handle MLB's contact-oriented hitting culture.",
        "body_jp": [
            "MLB打者はコンタクト能力を重視する傾向が強く、2ストライクからでもバットに当てる意識が強い。",
            "日本人投手は変化球で空振りを奪うスタイルが多く、この文化差への適応が初年度のカギとなる。",
            "特にストライクゾーン外の変化球をどれだけ振らせられるかが、奪三振率を左右する。",
            "今永昇太や山本由伸はこの適応に成功している代表例と言える。"
        ],
        "body_en": [
            "MLB hitters are strongly contact-oriented, often focused on putting the ball in play even with two strikes.",
            "Japanese pitchers typically chase whiffs with breaking balls, and bridging this cultural gap is a key rookie-year task.",
            "In particular, how often they can induce chases out of the zone drives their strikeout rate.",
            "Imanaga and Yamamoto are examples of pitchers who have adapted successfully."
        ]
    },
    {
        "slug": "ohtani-two-way-arsenal",
        "date": "2026-03-24", "category": "player", "tags": ["ohtani", "two-way"],
        "title_jp": "大谷の二刀流 — 使用球種の多様性",
        "title_en": "Ohtani the Two-Way Star: Pitch Arsenal Diversity",
        "summary_jp": "大谷翔平が投手として使う球種と、それぞれの被打率・空振り率を整理する。",
        "summary_en": "We lay out Ohtani's pitch arsenal and the batting-average-against and whiff rates on each.",
        "body_jp": [
            "大谷翔平の球種は4シーム、スイーパー、スプリット、カーブ、カッターと多様だ。",
            "4シームは平均96mph前後で、高めに決まるとほとんど振り遅れる。被打率.105は驚異的な数字だ。",
            "スイーパーはプレートを横断する大きな変化で、右打者へのアウトピッチとして機能する。",
            "スプリットは左打者にも機能し、奪三振ピッチとしての価値が高い。"
        ],
        "body_en": [
            "Ohtani's arsenal is diverse: 4-seam, sweeper, splitter, curve, and cutter.",
            "His 4-seam averages around 96 mph and, located up, beats hitters. A .105 BAA is staggering.",
            "The sweeper crosses the plate horizontally and is a putaway offering against RHHs.",
            "The splitter works vs. LHHs too — highly valued as a strikeout pitch."
        ]
    },
    {
        "slug": "imanaga-high-fastball",
        "date": "2026-03-23", "category": "player", "tags": ["imanaga", "fastball"],
        "title_jp": "今永の4シーム高め攻略",
        "title_en": "How Imanaga Wins With High Fastballs",
        "summary_jp": "今永昇太の4シーム高めゾーン攻略の有効性を、回転数とリリースポイントから説明する。",
        "summary_en": "We explain how Imanaga's high-zone 4-seam works, through spin rate and release point.",
        "body_jp": [
            "今永昇太の4シームは球速こそ平均的だが、リリースポイントの低さと高回転数により高めで威力を発揮する。",
            "打者からは浮き上がるように見えるため、ストライクゾーン高めに入れてもファウルや空振りを誘える。",
            "使用率44.5%と大きなウエイトを占めているが、被打率.163に抑えられている。",
            "この球を軸にスプリッターで仕留めるのが今永の基本パターンだ。"
        ],
        "body_en": [
            "Imanaga's 4-seam has only average velocity but thrives up in the zone thanks to a low release and high spin.",
            "Hitters perceive 'rise,' so even in-zone high pitches draw fouls and whiffs.",
            "He throws it 44.5% of the time yet limits the BAA to .163.",
            "Setting it up top then finishing with the splitter is Imanaga's bread-and-butter pattern."
        ]
    },
    {
        "slug": "murakami-low-slider-problem",
        "date": "2026-03-22", "category": "player", "tags": ["murakami", "slider"],
        "title_jp": "村上の低めスライダー対応",
        "title_en": "Murakami's Battle With Low Sliders",
        "summary_jp": "村上宗隆が直面するMLB投手の低めスライダー攻めに対する現時点の対応策を考察する。",
        "summary_en": "We consider how Murakami is handling MLB pitchers' low-slider attack so far.",
        "body_jp": [
            "左打者の村上宗隆に対して、MLB投手は対角線上の低めスライダーで勝負する傾向が強い。",
            "この攻め方に対してK% 32.1%は高い数字で、改善の余地がある。",
            "一方で見逃すケースが増えており、選球眼自体は機能している。BB% 19.3%がその証拠だ。",
            "ゾーン内の低めスライダーを見切れるようになれば、さらに打率とOPSが上がる可能性が高い。"
        ],
        "body_en": [
            "MLB pitchers often attack LHH Murakami with diagonal low sliders.",
            "His 32.1% K rate against this pattern is high, with room to improve.",
            "However, he takes many of these pitches — his plate discipline works, evidenced by a 19.3% BB rate.",
            "Learning to better recognize in-zone low sliders should boost his AVG and OPS further."
        ]
    },
    {
        "slug": "jp-war-career-rankings",
        "date": "2026-03-21", "category": "history", "tags": ["history", "war"],
        "title_jp": "MLB日本人選手 WAR累計ランキング",
        "title_en": "Japanese MLB Career WAR Rankings",
        "summary_jp": "日本人MLB選手の通算WAR上位を紹介し、ポジション別の評価もまとめる。",
        "summary_en": "We list Japanese MLB players at the top of career WAR and group them by position.",
        "body_jp": [
            "通算WARで見る日本人MLB選手の上位は、イチロー、ダルビッシュ有、野茂英雄、田中将大などが並ぶ。",
            "野手ではイチローが圧倒的で、投手ではダルビッシュ有と野茂英雄がしのぎを削る。",
            "現役では大谷翔平が投打両面で高いWARを稼ぐ異質な存在だ。",
            "今後10年で、大谷・山本由伸・今永昇太のWARがこのランキングをどう塗り替えるかが注目だ。"
        ],
        "body_en": [
            "By career WAR, the top Japanese MLB players include Ichiro, Darvish, Nomo, and Tanaka.",
            "Ichiro stands alone among position players; Darvish and Nomo contend at the top among pitchers.",
            "Among active players, Ohtani's unique two-way WAR accumulation stands apart.",
            "In the next decade, Ohtani, Yamamoto, and Imanaga will likely reshape this list."
        ]
    },
    {
        "slug": "gold-glove-jp-winners",
        "date": "2026-03-20", "category": "history", "tags": ["history", "gold-glove"],
        "title_jp": "ゴールドグラブ賞 日本人受賞者史",
        "title_en": "Japanese MLB Gold Glove Winners",
        "summary_jp": "ゴールドグラブ賞を受賞した日本人選手の一覧と、守備面での評価ポイントをまとめる。",
        "summary_en": "A list of Japanese MLB Gold Glove recipients and what set their defense apart.",
        "body_jp": [
            "ゴールドグラブ賞は、各ポジションで守備を評価される最高栄誉だ。日本人選手ではイチローが10回受賞している。",
            "イチローの受賞ポジションは右翼で、強肩と一塁送球の速さが評価された。",
            "投手では特定の年に受賞した選手もいるが、外野手ほど多くない。",
            "守備指標(DRS、UZR)の発展で、今後の評価はさらに客観化される見込みだ。"
        ],
        "body_en": [
            "The Gold Glove is the top defensive honor at each position. Ichiro has won it 10 times among Japanese players.",
            "Ichiro won as a right fielder, celebrated for his arm strength and quick throws to first.",
            "Some pitchers have won in specific years, but the count is smaller than outfielders.",
            "With DRS and UZR expanding, future awards should be judged more objectively."
        ]
    },
    {
        "slug": "rookie-watch-2026",
        "date": "2026-03-19", "category": "prospects", "tags": ["rookie", "prospects"],
        "title_jp": "新人王候補 2026 — 日本人選手の可能性",
        "title_en": "2026 Rookie of the Year: Japanese Candidates",
        "summary_jp": "2026年の新人王(ROTY)候補に挙がる日本人選手の現状と展望を整理する。",
        "summary_en": "We review Japanese candidates in the 2026 Rookie of the Year conversation.",
        "body_jp": [
            "2026年のROTY(新人王)には、複数の日本人選手が候補に挙がっている。",
            "村上宗隆は打撃指標で他候補をリードしており、シーズンを通じて活躍すればAL ROTYが現実味を帯びる。",
            "投手では、NPBからMLB入りした新人が序盤好投しており、NL ROTYも射程に入ってくる可能性がある。",
            "新人王は通常シーズン終盤の集計で決まるため、夏場以降の安定した成績が重要になる。"
        ],
        "body_en": [
            "Several Japanese players are in the 2026 ROTY conversation.",
            "Murakami leads most batting metrics among candidates; a full productive season puts the AL ROTY within reach.",
            "A pitcher coming over from NPB has started strong, putting NL ROTY on the table too.",
            "Because ROTY is decided by late-season totals, steady summer performance matters most."
        ]
    },
    {
        "slug": "postseason-jp-players",
        "date": "2026-03-18", "category": "team", "tags": ["postseason"],
        "title_jp": "ポストシーズン進出チームの日本人選手",
        "title_en": "Japanese Players on Postseason Contenders",
        "summary_jp": "2026年にポストシーズン進出が見込まれるチームに在籍する日本人選手を整理する。",
        "summary_en": "A roundup of Japanese players on 2026 postseason-contending rosters.",
        "body_jp": [
            "2026年ポストシーズン進出有力チームには複数の日本人選手が在籍している。",
            "ドジャース(大谷、山本)、パドレス(ダルビッシュ、松井裕樹)、カブス(鈴木、今永)などが代表例だ。",
            "10月に向けてコンディションを整えられるかが、ポストシーズンでの活躍を左右する。",
            "日本人選手同士のポストシーズン対決が実現する可能性も高まっている。"
        ],
        "body_en": [
            "Several Japanese players are on rosters likely to reach the 2026 postseason.",
            "Examples: Dodgers (Ohtani, Yamamoto), Padres (Darvish, Yuki Matsui), Cubs (Suzuki, Imanaga).",
            "Managing condition into October will be the key to postseason impact.",
            "Japanese-vs-Japanese postseason matchups are increasingly plausible."
        ]
    },
    {
        "slug": "jp-reliever-demand",
        "date": "2026-03-17", "category": "market", "tags": ["reliever", "market"],
        "title_jp": "日本人リリーバー需要の高まり",
        "title_en": "Rising MLB Demand for Japanese Relievers",
        "summary_jp": "近年MLBで日本人リリーバーの起用が増えている背景と、各球団の戦略を分析する。",
        "summary_en": "We analyze why MLB teams are increasingly signing Japanese relievers, and how they use them.",
        "body_jp": [
            "MLBでは短期契約で日本人リリーバーを獲得するケースが増えている。コスト対効果が高いためだ。",
            "スプリットやフォークといった変化球を武器にする投手は、MLB打者に対して優位性を持ちやすい。",
            "左投手の需要は特に高く、1イニング限定の起用でも価値がある。",
            "NPBからのポスティング以外に、メジャーリーガー契約後にマイナー経由で定着する選手も増えている。"
        ],
        "body_en": [
            "MLB teams increasingly sign Japanese relievers on short deals — the cost-benefit is strong.",
            "Pitchers with splitters and forkballs tend to hold an advantage against MLB hitters.",
            "Left-handers are especially in demand; even one-inning roles carry value.",
            "Beyond NPB postings, more players now lock in via minor-league deals that convert to majors."
        ]
    },
    {
        "slug": "midseason-outlook-2026",
        "date": "2026-03-16", "category": "team", "tags": ["outlook"],
        "title_jp": "2026シーズン中盤の予想と注目ポイント",
        "title_en": "2026 Midseason Outlook and Storylines",
        "summary_jp": "2026年シーズン中盤に向けた日本人選手と各球団の見どころを整理する。",
        "summary_en": "We map out midseason storylines to watch for Japanese players and teams in 2026.",
        "body_jp": [
            "開幕から1ヶ月が経過し、2026年シーズンの各球団・各選手の調子が見えてきた。",
            "大谷翔平の投打両面の数字、村上宗隆の新人としての適応、今永昇太の2年目ジンクス回避が注目点だ。",
            "チーム面ではドジャースとカブスの地区内での争い、パドレスのWild Card進出可能性がカギとなる。",
            "トレードデッドライン(7月末)に向けて、順位とロースター動向の両方を追う必要がある。"
        ],
        "body_en": [
            "One month into the season, we can see the early form of teams and players across MLB.",
            "Key storylines: Ohtani's two-way numbers, Murakami's rookie adjustment, and whether Imanaga avoids a sophomore slump.",
            "Team-wise: the Dodgers/Cubs divisional battles and the Padres' Wild Card potential.",
            "With the trade deadline at end of July, both standings and roster moves will demand attention."
        ]
    }
]

for a in ARTICLES:
    path = OUT / f"{a['slug']}.json"
    path.write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generated {len(ARTICLES)} articles at {OUT}")
