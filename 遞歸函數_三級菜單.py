main = {
    '台灣':{
        '台北':{
            '中和':{'大潤發':{}},
            '永和':{'豆漿':{}},
            '新店':{'釣蝦':{}}},
        '桃園':{
            '中壢':{'中央大學':{}},
            '青浦':{'高鐵站':{}},
            '桃園':{'IKEA':{}} },
        '高雄':{
            '左營':{'蓮池潭':{}},
            '楠梓':{'百慕達':{}},
            '小港':{'機場':{}},
            '岡山':{'羊肉':{}} }
    },
    '美國':{}
}


def thirdLvlMenu(dict):
    while 1:
        for k in dict: print(k)
        s = str(input('Enter the Area Name >>>>>>'))
        if s == 'b' or s == 'q' :return s
        elif s in dict and dict[s]:
            ret = thirdLvlMenu(dict[s])
            if ret =='q' :return 'q'
        elif s not in dict :continue
        elif dict[s]=={}:
            print('No more infos')
            continue



thirdLvlMenu(main)
