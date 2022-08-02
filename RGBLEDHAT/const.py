JMA_ICON_BASEURL = 'https://www.jma.go.jp/bosai/forecast/img/'
JMA_JSON_BASEURL = 'https://www.jma.go.jp/bosai/forecast/data/forecast/'


JMA_COLORS = {
    '100' : (0xff, 0x00, 0x00),
    '101' : (0xff, 0x99, 0x00),
    '102' : (0x00, 0xff, 0xff),
    '103' : (0x00, 0xff, 0xff),
    '104' : (0xff, 0xff, 0xff),
    '105' : (0xff, 0xff, 0xff),
    '106' : (0xff, 0xff, 0xff),
    '107' : (0xff, 0xff, 0xff),
    '108' : (0xff, 0xff, 0x00),
    '110' : (0xff, 0x99, 0x00),
    '111' : (0xff, 0x99, 0x00),
    '112' : (0x00, 0xff, 0xff),
    '113' : (0x00, 0xff, 0xff),
    '114' : (0x00, 0xff, 0xff),
    '115' : (0xff, 0xff, 0xff),
    '116' : (0xff, 0xff, 0xff),
    '117' : (0xff, 0xff, 0xff),
    '118' : (0xff, 0xff, 0xff),
    '119' : (0xff, 0xff, 0x00),
    '120' : (0x00, 0xff, 0xff),
    '121' : (0x00, 0xff, 0xff),
    '122' : (0x00, 0xff, 0xff),
    '123' : (0xff, 0xff, 0x00),
    '124' : (0xff, 0xff, 0xff),
    '125' : (0xff, 0xff, 0x00),
    '126' : (0x00, 0xff, 0xff),
    '127' : (0x00, 0xff, 0xff),
    '128' : (0x00, 0xff, 0xff),
    '130' : (0xff, 0x99, 0x00),
    '131' : (0xff, 0x99, 0x00),
    '132' : (0xff, 0x99, 0x00),
    '140' : (0xff, 0xff, 0x00),
    '160' : (0xff, 0xff, 0xff),
    '170' : (0xff, 0xff, 0xff),
    '181' : (0xff, 0xff, 0xff),
    '200' : (0xff, 0x99, 0x00),
    '201' : (0xff, 0x99, 0x00),
    '202' : (0x00, 0xff, 0xff),
    '203' : (0x00, 0xff, 0xff),
    '204' : (0xff, 0xff, 0xff),
    '205' : (0xff, 0xff, 0xff),
    '206' : (0xff, 0xff, 0xff),
    '207' : (0xff, 0xff, 0xff),
    '208' : (0xff, 0xff, 0x00),
    '209' : (0xff, 0x99, 0x00),
    '210' : (0xff, 0x99, 0x00),
    '211' : (0xff, 0x99, 0x00),
    '212' : (0x00, 0xff, 0xff),
    '213' : (0x00, 0xff, 0xff),
    '214' : (0x00, 0xff, 0xff),
    '215' : (0xff, 0xff, 0xff),
    '216' : (0xff, 0xff, 0xff),
    '217' : (0xff, 0xff, 0xff),
    '218' : (0xff, 0xff, 0xff),
    '219' : (0xff, 0xff, 0x00),
    '220' : (0x00, 0xff, 0xff),
    '221' : (0x00, 0xff, 0xff),
    '222' : (0x00, 0xff, 0xff),
    '223' : (0xff, 0x99, 0x00),
    '224' : (0x00, 0xff, 0xff),
    '225' : (0x00, 0xff, 0xff),
    '226' : (0x00, 0xff, 0xff),
    '228' : (0xff, 0xff, 0xff),
    '229' : (0xff, 0xff, 0xff),
    '230' : (0xff, 0xff, 0xff),
    '231' : (0x00, 0xff, 0xff),
    '240' : (0xff, 0xff, 0x00),
    '250' : (0xff, 0xff, 0xff),
    '260' : (0xff, 0xff, 0xff),
    '270' : (0xff, 0xff, 0xff),
    '281' : (0xff, 0xff, 0xff),
    '300' : (0x00, 0xff, 0xff),
    '301' : (0x00, 0xff, 0xff),
    '302' : (0x00, 0xff, 0xff),
    '303' : (0xff, 0xff, 0xff),
    '304' : (0xff, 0xff, 0xff),
    '306' : (0x00, 0x00, 0xff), # 大雨
    '308' : (0x00, 0x00, 0xff), # 暴風雨
    '309' : (0xff, 0xff, 0xff),
    '311' : (0x00, 0xff, 0xff),
    '313' : (0x00, 0xff, 0xff),
    '314' : (0xff, 0xff, 0xff),
    '315' : (0xff, 0xff, 0xff),
    '316' : (0xff, 0xff, 0xff),
    '317' : (0xff, 0xff, 0xff),
    '320' : (0x00, 0xff, 0xff),
    '321' : (0x00, 0xff, 0xff),
    '322' : (0xff, 0xff, 0xff),
    '323' : (0x00, 0xff, 0xff),
    '324' : (0x00, 0xff, 0xff),
    '325' : (0x00, 0xff, 0xff),
    '326' : (0xff, 0xff, 0xff),
    '327' : (0xff, 0xff, 0xff),
    '328' : (0x00, 0xff, 0xff),
    '329' : (0x00, 0xff, 0xff),
    '340' : (0xff, 0xff, 0xff),
    '350' : (0xff, 0xff, 0x00),
    '361' : (0xff, 0xff, 0xff),
    '371' : (0xff, 0xff, 0xff),
    '400' : (0xff, 0xff, 0xff),
    '401' : (0xff, 0xff, 0xff),
    '402' : (0xff, 0xff, 0xff),
    '403' : (0xff, 0xff, 0xff),
    '405' : (0x00, 0x00, 0xff), # 大雪
    '406' : (0xff, 0xff, 0xff),
    '407' : (0x00, 0x00, 0xff), # 暴風雪
    '409' : (0xff, 0xff, 0xff),
    '411' : (0xff, 0xff, 0xff),
    '413' : (0xff, 0xff, 0xff),
    '414' : (0xff, 0xff, 0xff),
    '420' : (0xff, 0xff, 0xff),
    '421' : (0xff, 0xff, 0xff),
    '422' : (0xff, 0xff, 0xff),
    '423' : (0xff, 0xff, 0xff),
    '425' : (0xff, 0xff, 0xff),
    '426' : (0xff, 0xff, 0xff),
    '427' : (0xff, 0xff, 0xff),
    '450' : (0xff, 0xff, 0xff),
}


JMA_TELOPS = {
    '100' : '晴れ',
    '101' : '晴時々曇',
    '102' : '晴一時雨',
    '103' : '晴時々雨',
    '104' : '晴一時雪',
    '105' : '晴時々雪',
    '106' : '晴一時雨か雪',
    '107' : '晴時々雨か雪',
    '108' : '晴一時雨か雷雨',
    '110' : '晴のち時々曇',
    '111' : '晴のち曇',
    '112' : '晴のち一時雨',
    '113' : '晴のち時々雨',
    '114' : '晴のち雨',
    '115' : '晴のち一時雪',
    '116' : '晴のち時々雪',
    '117' : '晴のち雪',
    '118' : '晴のち雨か雪',
    '119' : '晴のち雨か雷雨',
    '120' : '晴朝夕一時雨',
    '121' : '晴朝の内一時雨',
    '122' : '晴夕方一時雨',
    '123' : '晴山沿い雷雨',
    '124' : '晴山沿い雪',
    '125' : '晴午のちは雷雨',
    '126' : '晴昼頃から雨',
    '127' : '晴夕方から雨',
    '128' : '晴夜は雨',
    '130' : '朝の内霧のち晴',
    '131' : '晴明け方霧',
    '132' : '晴朝夕曇',
    '140' : '晴時々雨で雷を伴う',
    '160' : '晴一時雪か雨',
    '170' : '晴時々雪か雨',
    '181' : '晴のち雪か雨',
    '200' : '曇り',
    '201' : '曇時々晴',
    '202' : '曇一時雨',
    '203' : '曇時々雨',
    '204' : '曇一時雪',
    '205' : '曇時々雪',
    '206' : '曇一時雨か雪',
    '207' : '曇時々雨か雪',
    '208' : '曇一時雨か雷雨',
    '209' : '霧',
    '210' : '曇のち時々晴',
    '211' : '曇のち晴',
    '212' : '曇のち一時雨',
    '213' : '曇のち時々雨',
    '214' : '曇のち雨',
    '215' : '曇のち一時雪',
    '216' : '曇のち時々雪',
    '217' : '曇のち雪',
    '218' : '曇のち雨か雪',
    '219' : '曇のち雨か雷雨',
    '220' : '曇朝夕一時雨',
    '221' : '曇朝の内一時雨',
    '222' : '曇夕方一時雨',
    '223' : '曇日中時々晴',
    '224' : '曇昼頃から雨',
    '225' : '曇夕方から雨',
    '226' : '曇夜は雨',
    '228' : '曇昼頃から雪',
    '229' : '曇夕方から雪',
    '230' : '曇夜は雪',
    '231' : '曇海上海岸は霧か霧雨',
    '240' : '曇時々雨で雷を伴う',
    '250' : '曇時々雪で雷を伴う',
    '260' : '曇一時雪か雨',
    '270' : '曇時々雪か雨',
    '281' : '曇のち雪か雨',
    '300' : '雨',
    '301' : '雨時々晴',
    '302' : '雨時々止む',
    '303' : '雨時々雪',
    '304' : '雨か雪',
    '306' : '大雨',
    '308' : '暴風雨',
    '309' : '雨一時雪',
    '311' : '雨のち晴',
    '313' : '雨のち曇',
    '314' : '雨のち時々雪',
    '315' : '雨のち雪',
    '316' : '雨か雪のち晴',
    '317' : '雨か雪のち曇',
    '320' : '朝の内雨のち晴',
    '321' : '朝の内雨のち曇',
    '322' : '雨朝晩一時雪',
    '323' : '雨昼頃から晴',
    '324' : '雨夕方から晴',
    '325' : '雨夜は晴',
    '326' : '雨夕方から雪',
    '327' : '雨夜は雪',
    '328' : '雨一時強く降る',
    '329' : '雨一時みぞれ',
    '340' : '雪か雨',
    '350' : '雨で雷を伴う',
    '361' : '雪か雨のち晴',
    '371' : '雪か雨のち曇',
    '400' : '雪',
    '401' : '雪時々晴',
    '402' : '雪時々止む',
    '403' : '雪時々雨',
    '405' : '大雪',
    '406' : '風雪強い',
    '407' : '暴風雪',
    '409' : '雪一時雨',
    '411' : '雪のち晴',
    '413' : '雪のち曇',
    '414' : '雪のち雨',
    '420' : '朝の内雪のち晴',
    '421' : '朝の内雪のち曇',
    '422' : '雪昼頃から雨',
    '423' : '雪夕方から雨',
    '425' : '雪一時強く降る',
    '426' : '雪のちみぞれ',
    '427' : '雪一時みぞれ',
    '450' : '雪で雷を伴う',
}


JMA_AREA = {
    # # 北海道
    # '011000': '宗谷地方',
    # '012000': '上川・留萌地方',
    # '013000': '網走・北見・紋別地方',
    # # '014030': '十勝地方',
    # '014100': '釧路・根室地方',
    # '015000': '胆振・日高地方',
    # '016000': '石狩・空知・後志地方',
    # '017000': '渡島・檜山地方',
    # # 東北
    # '020000': '青森県',
    # '030000': '岩手県',
    # '040000': '宮城県',
    # '050000': '秋田県',
    # '060000': '山形県',
    # '070000': '福島県',
    # 関東甲信
    '080000': '茨城県',
    '090000': '栃木県',
    '100000': '群馬県',
    '110000': '埼玉県',
    '120000': '千葉県',
    '130000': '東京都',
    '140000': '神奈川県',
    '190000': '山梨県',
    # '200000': '長野県',
    # # 北陸',
    # '150000': '新潟県',
    # '160000': '富山県',
    # '170000': '石川県',
    # '180000': '福井県',
    # # 東海',
    # '210000': '岐阜県',
    # '220000': '静岡県',
    # '230000': '愛知県',
    # '240000': '三重県',
    # # 近畿',
    # '250000': '滋賀県',
    # '260000': '京都府',
    # '270000': '大阪府',
    # '280000': '兵庫県',
    # '290000': '奈良県',
    # '300000': '和歌山県',
    # # 中国（山口は除く）
    # '310000': '鳥取県',
    # '320000': '島根県',
    # '330000': '岡山県',
    # '340000': '広島県',
    # # 四国
    # '360000': '徳島県',
    # '370000': '香川県',
    # '380000': '愛媛県',
    # '390000': '高知県',
    # # 九州北部（山口を含む）
    # '350000': '山口県',
    # '400000': '福岡県',
    # '410000': '佐賀県',
    # '420000': '長崎県',
    # '430000': '熊本県',
    # '440000': '大分県',
    # # 九州南部・奄美
    # '450000': '宮崎県',
    # '460100': '鹿児島県（奄美地方除く）',
    # # '460040': '奄美地方',
    # # 沖縄
    # '471000': '沖縄本島地方',
    # '472000': '大東島地方',
    # '473000': '宮古島地方',
    # '474000': '八重山地方'
}