# -*- coding: utf-8 -*-
"""大阪版スポット定義 -> data/spots.json
YouTube大阪居酒屋動画10本(ヨウヤク堂在庫)から洗い出した梅田・難波・天満・京橋・新世界・新大阪等の名店29軒。
videos は data/videos.json のIDを参照。
座標: 国土地理院ジオコーディングAPI実測(番地レベル)。同ビル・同番地の店は微小オフセット。
sun: 日曜の営業時間(2026年7月調査、食べログ/ホットペッパー/公式サイト等)。
sun_class: lunch(日曜15時前に開店)/evening(15時以降開店)/closed(日曜定休)/unknown。
"""
import json, io

AREAS = [
    {"id": "umeda",     "name": "梅田・北新地・福島",       "color": "#e8543f"},
    {"id": "namba",     "name": "難波・心斎橋・大国町",     "color": "#3f7fd6"},
    {"id": "tenma",     "name": "天満・南森町",             "color": "#2f9e7d"},
    {"id": "kyobashi",  "name": "京橋・玉造上町",           "color": "#7b5cd6"},
    {"id": "south",     "name": "新世界・天下茶屋",         "color": "#e0489a"},
    {"id": "shinosaka", "name": "新大阪",                   "color": "#b07d2a"},
    {"id": "takatsuki", "name": "高槻",                     "color": "#708090"},
]

SPOTS = []
def add(slug, name, area, cat, lat, lng, approx, desc, videos, sun=None, sun_class=None, sun_note=None,
        tweets=None, links=None):
    s = {"slug": slug, "name": name, "area": area, "cat": cat,
         "lat": lat, "lng": lng, "approx": approx, "desc": desc, "videos": videos}
    if sun: s["sun"] = sun
    if sun_class: s["sun_class"] = sun_class
    if sun_note: s["sun_note"] = sun_note
    if tweets: s["tweets"] = tweets
    if links: s["links"] = links
    SPOTS.append(s)

# ---- 梅田・北新地・福島 ----
add("bishoku-maimon", "美食米門 梅田", "umeda", "洗練・創作", 34.700424, 135.495209, False,
    "一品一品が絶品のおしゃれな創作和食店（梅田2-2-22 ハービスPLAZA ENT 5F）。ハイクオリティな料理と洗練された空間で、デートや家族との大切な食事に最適。「大阪の神居酒屋7選」第7位。",
    ["WRUEaQ3V0b8"],
    sun="11:00〜15:00 / 17:00〜22:00", sun_class="lunch", sun_note="土日祝も平日と同一営業。不定休（ハービスPLAZA ENTに準ずる）")
add("yasu", "地酒だいにんぐ やす", "umeda", "洗練・創作", 34.703724, 135.502426, False,
    "休日問わず毎日大満席で、当日予約はほぼ不可能な梅田・堂山の隠れ家居酒屋（堂山町7-18 伊勢屋ビル3F）。創作料理と全国の地酒が圧倒的な美味しさと評判。",
    ["jM46YJkN5bY"],
    sun="18:00〜翌1:00", sun_class="evening", sun_note="不定休のため要予約確認。「18:00〜眠くなるまで」との記載も")
add("hanakujira", "おでん 花くじら 本店", "umeda", "おでん", 34.694580, 135.487122, False,
    "行列必至、大阪を代表するおでんの名店（福島2-8-2）。定番の大根やロールキャベツは並んででも食べる価値あり。「大阪の神居酒屋7選」第6位。",
    ["WRUEaQ3V0b8"],
    sun="16:00〜23:00", sun_class="evening", sun_note="日祝も休まず営業（L.O.22:30）。年末年始と8月は休業")
add("birichan2", "大衆酒場 びりちゃん2", "umeda", "立ち飲み・せんべろ", 34.698402, 135.499878, False,
    "大阪駅前第3ビルB1の超格安酒場（梅田1-1-3）。ハッピーアワーはレモンサワー88円・ハイボール99円。クリーミーな洋風ソースの「おでん大根」90円、半熟卵のスコッチエッグも外せない。",
    ["ryOYm3XFh5U"],
    sun="12:00〜23:00", sun_class="lunch", sun_note="土日祝12:00開店（平日14:00）。毎日18時までハッピーアワー")
add("inaseya", "立ち飲み いなせや 大阪駅前第3ビル店", "umeda", "立ち飲み・せんべろ", 34.698522, 135.499990, False,
    "ビール1杯350円から楽しめる駅前第3ビルの活気ある立ち飲み（梅田1-1-3 B1F）。おばんざい3種盛や刺身盛り合わせも揃い、名物「みそどてビフカツサンド」は絶対に注文すべき一品。",
    ["ryOYm3XFh5U"],
    sun="13:00〜22:30", sun_class="lunch", sun_note="土日13:00開店（平日15:00）。月曜定休")
add("sashisu", "すし酒場 さしす", "umeda", "海鮮・寿司", 34.698282, 135.499766, False,
    "駅前第3ビルB1の大行列すし酒場（梅田1-1-3）。あふれんばかりのトロが巻かれた名物「とろ鉄火巻」（1,078円）や、とろける「生ウニと国産牛の炙り」が絶品。",
    ["hQPyNuUHIQQ"],
    sun="12:00〜23:00", sun_class="lunch", sun_note="土日祝12:00開店（平日14:00）。不定休・年始休業あり")
add("hyozo", "ひょうそう（兵蔵）", "umeda", "大衆・名物", 34.697845, 135.495743, False,
    "物価高でも値上げせず、ほぼ全品350円で提供する北新地の最強コスパ居酒屋（曽根崎新地1-3-19 北新地ビルディング2F）。海鮮からお肉まで、安さだけでなく味もボリュームも大満足。",
    ["jM46YJkN5bY"],
    sun="定休日", sun_class="closed", sun_note="日曜定休。月〜土15:30〜24:00")
add("yamato", "酒場 やまと", "umeda", "大衆・名物", 34.702095, 135.500168, False,
    "コスパ抜群の梅田の酒場（小松原町2-4 大阪富国生命ビルB2F）。新鮮な刺身5種盛り（990円）やこだわりの明石焼き（690円）がおすすめ。現金のみ・行列必至。「大阪の神居酒屋7選」第5位。",
    ["WRUEaQ3V0b8"],
    sun="11:00〜22:00", sun_class="lunch", sun_note="毎日11:00〜22:00（L.O.21:00）。定休はビルに準ずる＋盆・年末年始")

# ---- 難波・心斎橋・大国町 ----
add("tekken", "哲剣（てっけん）", "namba", "バル・個性派", 34.661575, 135.500565, False,
    "見取り図・盛山さんのNo.1おすすめ店（難波中2-8-86）。アヒージョや前菜盛り合わせなど「全メシが美味い」と豪語するカジュアルイタリアンバル。非常に人気のため予約推奨。",
    ["zjgwj4qw_QE"],
    sun="定休日", sun_class="closed", sun_note="日曜定休（月曜祝日の場合は日曜営業・月曜休の振替あり）。月〜土祝17:00〜23:30")
add("mitsuwaya", "みつわや酒店", "namba", "大衆・名物", 34.656593, 135.499207, False,
    "見取り図・リリーさんのNo.1おすすめ店（大国町・敷津東2-4-4）。木津卸売市場のそばで深夜3時から昼12時まで営業する超個性派。安くて新鮮な魚が朝方から楽しめる昭和レトロな大衆酒場。",
    ["zjgwj4qw_QE"],
    sun="定休日", sun_class="closed", sun_note="日曜定休（木津市場の休みに準ずる）。平日は深夜3:00〜昼12:00＋17:00〜20:30（開店時刻は情報源により3:00/5:00と揺れあり）")
add("tegetege", "居酒屋 てげてげ", "namba", "大衆・名物", 34.662197, 135.509155, False,
    "チキン南蛮など絶品の宮崎料理が楽しめる、若手芸人の打ち上げ定番店（日本橋東1-1-9）。鍋や辛麺など南九州の味が揃う。",
    ["zjgwj4qw_QE"],
    sun="18:00〜22:00", sun_class="evening", sun_note="全曜日18:00〜22:00営業")
add("atariya", "立ち呑み あたりや食堂 なんば店", "namba", "立ち飲み・せんべろ", 34.666206, 135.499298, False,
    "天ぷらや新鮮な魚介が絶品の、一品ごとのクオリティが非常に高い立ち飲み屋（難波4-6-5）。見取り図もおすすめする名店。",
    ["zjgwj4qw_QE"],
    sun="15:00〜24:00", sun_class="evening", sun_note="全曜日15:00〜24:00（L.O.23:30）・定休なし。閉店時刻は〜翌1:00表記の情報源もあり")
add("hidezo", "魚屋ひでぞう 別館", "namba", "海鮮・寿司", 34.664196, 135.504074, False,
    "魚の卸業を営む会社が経営する新鮮魚介の人気店（難波千日前4-19 2F）。雲丹と湯葉、お造り、牡蠣のスープ、寿司など贅沢な構成の飲み放題付き5,000円コースが超高コスパ。",
    ["aPsidzKkSxk"],
    sun="15:00〜23:00", sun_class="evening", sun_note="火曜定休。近隣に立ち呑み店・難波店などの系列あり")
add("nakamoto", "鮨 なかもと", "namba", "海鮮・寿司", 34.664646, 135.505157, False,
    "赤酢のシャリを使った本格寿司を1貫250円〜とリーズナブルに楽しめるおしゃれな寿司居酒屋（難波千日前4-35）。カワハギ肝和えや白海老・のどぐろが人気でデートにも最適。ひでぞうグループ。",
    ["aPsidzKkSxk"],
    sun="17:00〜23:00", sun_class="evening", sun_note="全曜日17:00〜23:00（L.O.22:30）・不定休")
add("kadoya", "豚足のかどや", "namba", "大衆・名物", 34.665440, 135.498337, False,
    "旨味が爆発する「豚足」が名物のディープな大衆居酒屋（難波中1-4-15）。お買い物帰りの一杯に最適で、昼から格安で絶品グルメとビールが楽しめる。「大阪の神居酒屋7選」第3位。",
    ["WRUEaQ3V0b8", "W3sB3tmf4o4"],
    sun="11:00〜22:00", sun_class="lunch", sun_note="2025年2月から無休（旧情報では火曜定休）。L.O.21:30")
add("hide", "和洋酒菜 ひで", "namba", "洗練・創作", 34.671654, 135.502274, False,
    "お酒好きから圧倒的に支持されている、絶品和洋折衷料理の最高峰（心斎橋筋2-1-3）。完全予約制のカウンター6席。「大阪の神居酒屋7選」堂々の第1位。",
    ["WRUEaQ3V0b8"],
    sun="13:00〜（2部制 13:00/17:00）", sun_class="lunch", sun_note="完全予約制。土日は1部13:00/2部17:00の2回転（一休の予約枠で確認）")

# ---- 天満・南森町 ----
add("marcus", "あずき色のマーカス", "tenma", "立ち飲み・せんべろ", 34.706261, 135.511780, False,
    "路地裏に静かに佇む、大人の隠れ家のような立ち飲み店（天神橋4-12-11）。全国から厳選された豊富な日本酒と、それに合わせる工夫を凝らしたアテが揃う。ちょい飲み・はしご酒に最適。",
    ["_AnT6QnwSog"],
    sun="15:00〜23:00", sun_class="evening", sun_note="定休は年末年始のみ。閉店時刻は23:00/23:30と情報源に揺れあり")
add("daiyame", "備長炉端 だいやめ 天満店", "tenma", "海鮮・寿司", 34.704433, 135.511002, False,
    "目の前で焼き上げる臨場感抜群の炉端焼き（天神橋4-8-6 サンプラザビル6F）。「特大えび」やじっくり焼かれた「ぶりの原始焼き」が格別。天満で海鮮を食べるなら外せない名店。",
    ["_AnT6QnwSog"],
    sun="12:00〜23:30", sun_class="lunch", sun_note="土日祝12:00開店。月曜定休（祝日の場合は翌火曜休）")
add("kamonn", "IZAKAYA KAMONN", "tenma", "海鮮・寿司", 34.709511, 135.511841, False,
    "釣り好きの店主が自ら釣った超新鮮な魚介を堪能できる居酒屋（天神橋6-5-27）。名物「アジフライ」は圧倒的な美味しさ。2階では釣具も販売。",
    ["_AnT6QnwSog"],
    sun="17:00〜翌1:00", sun_class="evening", sun_note="不定休（釣行等）。Instagramで当日確認推奨")
add("gogasha53", "大衆居酒屋 GoGASHA53", "tenma", "おでん", 34.699879, 135.511536, False,
    "おしゃれな雰囲気の天満の人気店（天神橋3-2-23）。関西風の上品な出汁が染みた「おでん 大根と厚揚げ」（358円）と、天ぷら風に揚げたナスに麻婆餡をかけたオリジナル「サクサク麻婆茄子」（499円）が名物。",
    ["koibspoNzoY"],
    sun="13:00〜23:00", sun_class="lunch", sun_note="日祝13:00〜23:00（料理L.O.22:00）。一部不定休あり")
add("naodaime", "お魚と日本酒 七代目なお 天満店", "tenma", "海鮮・寿司", 34.703590, 135.511490, False,
    "海鮮に特化した深夜3時まで営業の活気あふれる店（天神橋4-6-19）。お通しにタイ・イサキ・ヒラメ・ハマチの豪華刺身4点盛りが出てくる。白子ポン酢や大粒の生牡蠣も絶品。",
    ["koibspoNzoY"],
    sun="16:00〜翌3:00", sun_class="evening", sun_note="定休は隔週水曜のため日曜は営業。休みはInstagramで告知")
add("torosaba", "大衆酒場 とろ鯖 南森町店", "tenma", "海鮮・寿司", 34.698662, 135.511597, False,
    "サバ料理を全面に押し出す専門店（天神橋3-2-37）。サバの脂と旨みが凝縮された濃厚な「鯖出汁の湯豆腐」（380円）や、脂の乗りが抜群の「とろさば塩焼き」が絶品。SABAR系列の大衆酒場業態。",
    ["koibspoNzoY"],
    sun="12:00〜23:30", sun_class="lunch", sun_note="土日祝12:00開店。定休は年末年始のみ")

# ---- 京橋・玉造上町 ----
add("toyo", "居酒屋 とよ", "kyobashi", "立ち飲み・せんべろ", 34.697193, 135.535370, False,
    "国内外から観光客が押し寄せる京橋の大人気青空立ち飲み屋台（東野田町3-2-26）。名物大将がガスバーナーで豪快に炙るマグロやいくらを格安で楽しめる。飲み物や箸はセルフサービス。「大阪の神居酒屋7選」第2位。",
    ["WRUEaQ3V0b8", "RDaMAhr6LPU"],
    sun="定休日", sun_class="closed", sun_note="営業は火水金13:00〜19:00・土12:00〜19:00のみ。月木日祝定休")
add("nagahori", "ながほり", "kyobashi", "洗練・創作", 34.676514, 135.525726, False,
    "芸能人もお忍びで通う、丁寧につくられた料理が「天才的」な隠れ名店（上町1-3-9・玉造駅徒歩約10分）。「大阪の神居酒屋7選」第4位。",
    ["WRUEaQ3V0b8"],
    sun="定休日", sun_class="closed", sun_note="日・月・祝定休。火〜金17:00〜22:00・土13:00〜22:00")

# ---- 新世界・天下茶屋 ----
add("tengu", "てんぐ", "south", "大衆・名物", 34.649773, 135.506073, False,
    "新世界ジャンジャン横丁の老舗串かつ店（恵美須東3-4-12）。白味噌ベースで柔らかく煮込まれた名物「どて焼き」と、サクサク衣の「串かつ」「エビ」を二度漬け禁止のソースで。これぞ大阪の味。",
    ["hQPyNuUHIQQ"],
    sun="10:30〜20:00", sun_class="lunch", sun_note="月曜定休。火〜日10:30〜20:00（L.O.19:00）")
add("maruyone", "おでん まる米", "south", "おでん", 34.638176, 135.496262, False,
    "具材によって出汁を変える並々ならぬこだわりのおでん屋（天下茶屋・花園南2-7-30）。〆にいただく名物「とう飯（豆腐をご飯に乗せたもの）」はここでしか味わえない必食メニュー。",
    ["jM46YJkN5bY"],
    sun="12:00〜21:00", sun_class="lunch", sun_note="毎日12:00〜21:00（L.O.20:30）。盆・正月休み・臨時休業あり")

# ---- 新大阪 ----
add("fuji", "魚屋スタンドふじ", "shinosaka", "海鮮・寿司", 34.731777, 135.498444, False,
    "「海鮮が安いだけの店」がコンセプトの超高コスパ店（新大阪駅地下・新なにわ大食堂内）。トロさわら（638円）など高品質な魚介が低価格で楽しめる。出張や旅行の合間に最適。",
    ["aPsidzKkSxk"],
    sun="11:30〜23:00", sun_class="lunch", sun_note="全曜日11:30〜23:00（L.O.22:00）・無休")
add("kawakita", "川北商店 新大阪店", "shinosaka", "大衆・名物", 34.731900, 135.498560, False,
    "新大阪駅地下の焼き鳥店（新なにわ大食堂内）。ビール・小鉢・串盛り5本付き「ちょい飲み焼き盛りセット」1,518円が人気。ラーメン屋レベルのクリーミーな絶品スープの「鶏そば定食」（1,188円）もおすすめ。",
    ["aPsidzKkSxk"],
    sun="10:00〜23:00", sun_class="lunch", sun_note="全曜日10:00〜23:00（L.O.21:45）。定休は施設に準ずる")

# ---- 高槻 ----
add("stand-b", "スタンドB", "takatsuki", "バル・個性派", 34.850071, 135.621201, True,
    "国産の生牡蠣をはじめとする牡蠣料理の食べ放題＋飲み放題が4,480円〜という破格の牡蠣スタンド（高槻市高槻町14-8）。カキフライから創作料理、冬の牡蠣鍋と〆の雑炊まで牡蠣を心ゆくまで堪能できる。",
    ["jM46YJkN5bY"],
    sun="12:00〜翌0:00", sun_class="lunch", sun_note="不定休。食べ飲み放題は通常4,980円（17時台/21時以降の予約で4,480円）。※動画では店舗所在地の明言がなく、条件に合致する唯一の店として高槻店を掲載")

# ==== Xで話題の酒場21選（Xフルアーカイブ 2025/7〜2026/7 高エンゲージ投稿より、日曜営業はGoogle Maps 2026年7月時点） ====

# ---- キタ（梅田・お初天神・北新地） ----
add("sakatoke", "サカトケ乃カミ", "umeda", "立ち飲み・せんべろ", 34.705898, 135.497421, False,
    "旬魚と日本酒の人気立ち飲み（芝田1-3-7）。「8歳の息子と立ち飲みに入ったら常連客に温かく迎えられた」投稿が2026年4月に大拡散し、大阪全体の年間最大バズ（18,449いいね）に。名物は中身おまかせの「パンドラの箱」。Google 4.1（359件）。",
    [],
    sun="13:30〜24:00", sun_class="lunch",
    tweets=[{"id": "2043923731257667601", "handle": "tadashi754take", "likes": "18,449"}],
    links=[{"label": "公式HP", "url": "https://www.shokuetudou.com/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=7960692616354601937"}])
add("sashisu-shinume", "すし酒場 さしす 新梅田食道街店", "umeda", "海鮮・寿司", 34.703907, 135.497910, False,
    "開店前から行列の寿司酒場・新梅田食道街店（角田町9-26）。「人気は映えだけじゃない」と分析するレポ（レモンサワー190円・うにく649円）が3,500いいね超え。名物こぼれ中とろは脳を揺らす迫力。昼飲みの定番。Google 4.5（57件）。",
    [],
    sun="12:00〜23:00", sun_class="lunch",
    tweets=[{"id": "2069978385808572647", "handle": "osaka2shin", "likes": "3,561"}],
    links=[{"label": "新梅田食道街HP", "url": "https://shinume.com/shop/%E7%AB%8B%E3%81%A1%E3%81%99%E3%81%97%E9%85%92%E5%A0%B4-%E3%81%95%E3%81%97%E3%81%99%E3%80%80%E6%96%B0%E6%A2%85%E7%94%B0%E9%A3%9F%E9%81%93%E8%A1%97%E5%BA%97/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=8783735119009254136"}])
add("chiruchiru", "ちるちるにびる", "umeda", "バル・個性派", 34.698402, 135.498413, False,
    "「迷宮みたいな駅前第2ビル地下2階」の立ち飲み中華バル（梅田1-2-2 B2F）。痺れと辛さが絶妙な麻婆豆腐、黒酢酢豚、牡蠣クリーム春巻き。小皿590円〜であれこれ頼めるのが罪。開店前から並ぶ人気。Google 4.2（92件）。",
    [],
    sun="15:00〜22:45", sun_class="evening",
    tweets=[{"id": "2049768539859669109", "handle": "Linasuke0508", "likes": "1,970"}],
    links=[{"label": "Google Map", "url": "https://maps.google.com/?cid=17828072376846180429"}])
add("masa", "大衆すし居酒屋 まさ", "umeda", "海鮮・寿司", 34.698500, 135.498530, False,
    "「梅田で昼飲み×海鮮ならここ」と拡散（駅前第2ビルB2F 41号）。厚切りのお造りと黒毛和牛たたき、寿司10貫定食980円のコスパが売り。※Google評価は3.7（201件）と割れており、鮮度への辛口レビューもあるため過度な期待は禁物。",
    [],
    sun="12:00〜21:00", sun_class="lunch",
    tweets=[{"id": "2051911765949313251", "handle": "reiranran9214", "likes": "1,555"}],
    links=[{"label": "公式HP", "url": "https://tachinomi-masa.com/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=6852366478068936322"}])
add("gold", "フレンチ酒場 GOLD 梅田店", "umeda", "バル・個性派", 34.702721, 135.502548, False,
    "東通商店街のカジュアルフレンチ（堂山町4-16）。極薄生ハム、トリュフバターの禁断シュウマイ、和牛カルパッチョを酒場価格で。1階カウンター・2階テーブル、予約推奨。Google 4.2（588件）。",
    [],
    sun="12:00〜翌1:00", sun_class="lunch",
    tweets=[{"id": "2078491337662554257", "handle": "sukiya_nen_", "likes": "461"}],
    links=[{"label": "公式HP", "url": "https://french-sakaba-gold.jp/umeda/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=15818966177585290670"}])
add("neo-tiger", "大衆酒場 北新地Neoタイガー", "umeda", "大衆・名物", 34.697959, 135.498634, False,
    "高級街・北新地のど真ん中でタコハイ109円・ビール219円という逆張り価格が話題（曾根崎新地1-11-7）。「この値段で北新地、大丈夫！？」レビュー多数。仕事帰りのサラリーマンの聖地化が進行中。平日は朝5時まで。Google 4.0（176件）。",
    [],
    sun="17:00〜24:00", sun_class="evening",
    tweets=[{"id": "2077770862107992122", "handle": "ueda4649", "likes": "106"}],
    links=[{"label": "公式HP", "url": "https://kemt500.gorp.jp/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=14869833650533477236"}])
add("umaru", "大衆馬肉酒場 うまる 梅田お初天神店", "umeda", "大衆・名物", 34.700462, 135.500473, False,
    "お初天神表参道の馬肉専門酒場（曾根崎2-11-22 2F）。ドリンク99円のハッピーアワー投稿がXで拡散。臭みゼロの馬刺し盛りとユッケが高評価で、Google 4.6（326件）はキタ勢トップクラス。17〜19時・22時〜は料理も半額帯。",
    [],
    sun="12:00〜23:00", sun_class="lunch",
    tweets=[{"id": "2079117644620595514", "handle": "crew_value1"}],
    links=[{"label": "ホットペッパー", "url": "https://www.hotpepper.jp/strJ004090749/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=6550274978308180759"}])

# ---- ミナミ（難波・裏なんば・道頓堀・心斎橋） ----
add("mataraiya", "焼肉酒場 又来家", "namba", "大衆・名物", 34.666470, 135.504013, False,
    "「分厚いステーキみたいな肉が柔らかくて飲み放題の酒も濃い」レポが千いいね超えの焼肉酒場（千日前2-9-6 リップル千日前センタービル2F）。上質和牛を酒場価格で出す広々個室スタイルで、グループ利用の口コミ評価が高い。オンライン予約可。Google 4.6（495件）。",
    [],
    sun="12:00〜23:00", sun_class="lunch",
    tweets=[{"id": "2062519167073554505", "handle": "usamiiin", "likes": "1,439"}],
    links=[{"label": "公式HP", "url": "https://mataraiya-yakiniku.com/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=15019882631749924283"}])
add("shingo", "すし居酒屋 しんご", "namba", "海鮮・寿司", 34.671375, 135.504349, False,
    "「人生で1番通ってる店」という外食1492回のグルメ垢の投稿がバズった寿司居酒屋（東心斎橋2-4-19 玉屋町ギャラクシービル3号館1F）。大将の人柄と鮮度で海外観光客のレビューも絶賛一色、Google 4.8（194件）はミナミ勢トップ。入口が分かりにくい隠れ家。",
    [],
    sun="定休日", sun_class="closed", sun_note="日曜定休（月〜土17:30〜23:30営業）",
    tweets=[{"id": "2047841568267309202", "handle": "yk_mg18", "likes": "1,416"}],
    links=[{"label": "公式HP", "url": "https://kdvg000.gorp.jp/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=12056036823935088545"}])
add("aaaa", "ああああ", "namba", "立ち飲み・せんべろ", 34.663780, 135.502792, False,
    "RPGの主人公みたいな店名の看板なし立ち飲み（難波千日前15-19 油谷ビル3F）。「全品1,000円以下。実にうまい」と2度バズ（1,196・909いいね）。いわしのモンブランや蟹味噌クリームコロッケなど創作系が強く、週末は常時待ちの人気。Google 4.6（16件）。",
    [],
    sun="17:00〜24:00", sun_class="evening",
    tweets=[{"id": "2059229615504437629", "handle": "ad_career28", "likes": "1,196"}],
    links=[{"label": "Google Map", "url": "https://maps.google.com/?cid=15538552961901480625"}])
add("rikusui", "生産者直営 海鮮居酒屋 Rikusui", "namba", "海鮮・寿司", 34.669483, 135.501663, False,
    "中トロ・とらふぐ3時間食べ放題6,050円（女性千円引き）の投稿がバズった海鮮居酒屋（心斎橋筋2-3-15 戎橋NORTHビル5F）。生産者直営で、焼きフグのお通しから始まるQRオーダー式。食べ放題の質は口コミで賛否あるので、コース選びは慎重に。Google 4.2（883件）。",
    [],
    sun="16:00〜23:00", sun_class="evening",
    tweets=[{"id": "2069739710533243085", "handle": "osakagourmet4", "likes": "719"}],
    links=[{"label": "ホットペッパー", "url": "https://www.hotpepper.jp/strJ003624554/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=215750310012842113"}])
add("hidezo-tachinomi", "魚屋ひでぞう 立ち呑み", "namba", "立ち飲み・せんべろ", 34.664459, 135.503983, False,
    "造り三種580円・生カキポン酢580円・おまかせ五貫880円の海鮮立ち飲み（難波千日前9-1）。「刺身はどれも新鮮でコスパ抜群、いつも行列」のレポでバズ。裏なんばの海鮮立ち飲みの代名詞的存在で、市場直送ネタが日替わり。Google 4.2（472件）。",
    [],
    sun="15:00〜24:00", sun_class="evening",
    tweets=[{"id": "2073024721399234801", "handle": "nnstable", "likes": "529"}],
    links=[{"label": "Google Map", "url": "https://maps.google.com/?cid=12743576623859092201"}])
add("minaminami", "天ぷらとすし酒場 みなみなみ", "namba", "海鮮・寿司", 34.663895, 135.503174, False,
    "2026年4月開店の新店（難波千日前14-22 イレブンハイツ1F）。寿司2貫180円〜・天ぷら120円〜で「シャリが小さくていくらでも食べれる」とバズ。18時までのハッピーアワーと梅酒ソーダ373円（みなみ）の語呂遊びも人気。裏なんばど真ん中。Google 4.3（30件）。",
    [],
    sun="15:00〜23:00", sun_class="evening",
    tweets=[{"id": "2061673141257322901", "handle": "todo184", "likes": "473"}],
    links=[{"label": "Google Map", "url": "https://maps.google.com/?cid=1784046433070548512"}])
add("tachizushi-nakamoto", "立ち鮨 なかもと", "namba", "海鮮・寿司", 34.665955, 135.504578, False,
    "予約困難な高級鮨「鮨なかもと」の立ち食い業態として2026年1月開店（千日前2-3-24 久富千日プラザ1F）。毛蟹450円・肝のせカワハギ350円に「ヤヴァい」の一言レポがバズ。1貫100円台から本格鮨をつまめる、ひでぞうグループの新星。Google 4.4（35件）。",
    [],
    sun="15:00〜23:00", sun_class="evening", sun_note="木曜定休",
    tweets=[{"id": "2061712949530784164", "handle": "tabichef", "likes": "455"}],
    links=[{"label": "Instagram", "url": "https://www.instagram.com/sushi_nakamoto01"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=8316300846000017542"}])

# ---- 天満（裏天満・天神橋筋） ----
add("xavier", "無敵のザビエル", "tenma", "バル・個性派", 34.703411, 135.511505, False,
    "「どの高級中華より感動した。凄まじくクリエイティブなのに全品千円以下」という投稿が千いいね超えの創作中華居酒屋（天神橋4-6-17）。名物は旨味たっぷりの麻婆豆腐と黄金ピータン。天満の年間グルメバズ首位。Google 4.8（33件）。",
    [],
    sun="定休日", sun_class="closed", sun_note="日曜定休（土曜は12:00〜23:30営業）",
    tweets=[{"id": "2047958236582846661", "handle": "hiroyukikishi", "likes": "1,047"}],
    links=[{"label": "Instagram", "url": "https://www.instagram.com/mutekinoxavier/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=8732810730672519435"}])
add("gifuya", "大衆酒場 ぎふや 裏天満店", "tenma", "大衆・名物", 34.706974, 135.512970, False,
    "生ビール176円・から揚げ429円の会計レポが繰り返しバズる裏天満の代表格（池田町7-1）。創業100年系の串カツと名物どろ炊きが人気で、名古屋から遠征するファンも。昼12時から通し営業。Google 4.5（155件）。",
    [],
    sun="11:30〜23:00", sun_class="lunch",
    tweets=[{"id": "2050542775083712603", "handle": "Uzusio_Tatsuya", "likes": "608"}],
    links=[{"label": "ホットペッパー", "url": "https://www.hotpepper.jp/strJ003298930/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=12893303845543766012"}])
add("tenma-sakagura", "天満酒蔵", "tenma", "大衆・名物", 34.706623, 135.511292, False,
    "創業56年、昼から大瓶400円の老舗大衆酒場（天神橋5-7-28）。マンガ「ソロ酔い酒場」の舞台として繰り返し話題になり、テレビ酒場番組にも登場。おでん盛り400円・きずし280円の昭和価格。渋い老舗ゆえ点数より空気を楽しむ店（Google 3.7・605件）。",
    [],
    sun="11:30〜21:30", sun_class="lunch", sun_note="火・金定休",
    tweets=[{"id": "2074310130611749301", "handle": "1000bero_net", "likes": "294"}],
    links=[{"label": "公式HP", "url": "http://tenmasakagura.com/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=12113388735368868049"}])
add("butamon", "ぶたもん 天満店", "tenma", "大衆・名物", 34.705494, 135.511963, False,
    "天満駅1分、1階立ち飲み・2階テーブルの二毛作やきとん（天神橋4-12-27）。臭みのないレバステーキとハツ刺し、濃いめハイボールのせんべろセットが名物で、はしご酒レポの常連。オフ会会場としても指名される。Google 4.1（239件）。",
    [],
    sun="11:00〜23:00", sun_class="lunch",
    tweets=[{"id": "2051989203240784196", "handle": "RDG_P2s", "likes": "277"}],
    links=[{"label": "Instagram", "url": "https://www.instagram.com/tenma_butamon/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=2058946506231717100"}])
add("shurakudo", "天満酒楽堂", "tenma", "海鮮・寿司", 34.707554, 135.512039, False,
    "市場直送鮮魚と47都道府県の日本酒60種（天神橋5-2-10）。喧騒の天満で一歩入ると落ち着いたシックな空間に変わる二面性が持ち味。平日20時で満席・予約なし入店お断りの報告があるため予約推奨。Google 4.6（177件）。",
    [],
    sun="17:00〜24:00", sun_class="evening",
    tweets=[{"id": "2077074252604600804", "handle": "mahjong_oniku", "likes": "215"}],
    links=[{"label": "食べログ", "url": "https://tabelog.com/osaka/A2701/A270103/27145628/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=6498648263260273128"}])
add("umematsu", "とりさし梅松 天満店", "tenma", "立ち飲み・せんべろ", 34.705982, 135.511307, False,
    "鹿児島ブランドのとりさし専門立ち飲み（天神橋4-10-19）。せんべろセットと皮トロレア炭火焼きが「安くて美味い」と評判で、Google 4.8×1,167件は今回の14軒で最強の評価。鹿児島焼酎と甘口九州醤油の組み合わせが正解。",
    [],
    sun="11:00〜18:30", sun_class="lunch", sun_note="早じまい注意",
    tweets=[{"id": "2077249792204554491", "handle": "kanpa____i", "likes": "53"}],
    links=[{"label": "Instagram", "url": "https://www.instagram.com/torisashi.umematsu.tenma"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=18144726801786428325"}])
add("muni", "大衆酒場 むに 大阪天満店", "tenma", "大衆・名物", 34.707027, 135.512604, False,
    "2025年9月開店のネオン大衆酒場（池田町6-18）。A5和牛の肉手毬寿司と飲むほど容量が増える「出世サワー」がSNS映えで急成長。16〜18時入店でサワー90円のハッピーアワーあり。Google 4.8（816件）※食べログ3.06との乖離が大きく、映え重視で楽しむ店。",
    [],
    sun="12:00〜翌2:00", sun_class="lunch",
    tweets=[{"id": "2077821211846013215", "handle": "TENCHO_777", "likes": "49"}],
    links=[{"label": "公式HP", "url": "https://muni-tenma.owst.jp/"}, {"label": "食べログ", "url": "https://tabelog.com/osaka/A2701/A270103/27150951/"}, {"label": "Google Map", "url": "https://maps.google.com/?cid=10025413216440185919"}])

# ---- validation & output ----
videos = json.load(io.open('data/videos.json', encoding='utf-8'))
bad = [(s['slug'], v) for s in SPOTS for v in s['videos'] if v not in videos]
print('video refs not found:', bad if bad else 'none')
slugs = [s['slug'] for s in SPOTS]
assert len(slugs) == len(set(slugs)), 'duplicate slug'
for s in SPOTS:
    assert s['area'] in {a['id'] for a in AREAS}, 'bad area: ' + s['slug']
    assert s.get('sun') and s.get('sun_class'), 'missing sun: ' + s['slug']

json.dump({"areas": AREAS, "spots": SPOTS}, io.open('data/spots.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote data/spots.json  spots:', len(SPOTS), ' areas:', len(AREAS))
