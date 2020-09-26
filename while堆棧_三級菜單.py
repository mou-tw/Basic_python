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

l=[main]


while l :
    #for i in l[0].keys():print(i) 等同下句功能
    for k in l[0]:print(k)
    s = str(input('Enter the Area Name >>>>>'))
    if s in l[-1] and l[-1][s] :
        l.append(l[-1][s])
    elif s in l[-1] and l[-1][s]=={} :
        print('No more Info')
    elif s == 'b':
        l.pop()
    elif s == 'q':
        break
    else: continue