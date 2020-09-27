import re

def caculate(s):
    if '/' in s:
        a,b = s.split('/')
        return str(float(a) / float(b))
    if '*' in s:
        if s.count('-') == 1:
            a, b = s.split('*')
            return str(float(a) * float(b))
        if s.count('-') == 2:
            a, b = s.split('*')
            return '+'+ str(float(a) * float(b))
        else:
            a, b = s.split('*')
            return str(float(a) * float(b))
    if '+' in s:
        a, b = s.split('+')
        return str(float(a) + float(b))
    if '-' in s:
        if len(s.split('-'))==2:
            a, b = s.split('-')
            return str(float(a) - float(b))
        if len(s.split('-'))==3:
            a,b,c = s.split('-')
            b =float(b)*-1
            return str(float(b)- float(c))

def dealwithInside(s):
    s = s.strip(' ()')
    print('執行乘除')
    while '/'in s or'*'in s:
        ret = re.search('[-]?\d+\.?\d*[*/][-]?\d+\.?\d*',s)
        print(ret.group())
        ret1 = caculate(ret.group())
        s = s.replace(ret.group(),ret1)
        print(s)
        if '-' in s and len(s.split('-')) ==2 and s.split('-')[0] == '' :
            print('執行完畢')
            return s
    print('執行加減')
    while '-'in s or '+'in s:
        ret = re.search('[-]?\d+\.?\d*[+-]\d+\.?\d*', s)
        print(ret.group())
        ret1 = caculate(ret.group())
        s = s.replace(ret.group(),ret1)
        print(s)
        if '-' in s and len(s.split('-')) ==2 and '+' not in s:
            break
    print('執行完畢')
    return s


s = "1 - 2 * ( (60-30 +(-40/5*8-2) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
s = s.replace(' ','')
print(s)

while '(' in s:
    ret = re.search('\([^()]+\)', s)
    print(ret.group())
    ret1 = dealwithInside(ret.group())
    s = s.replace(ret.group() ,ret1).replace('+-','-').replace('--','+')
    print(s)
    print()
final_ans = dealwithInside(s)
print(final_ans)
print(1 - 2 * ( (60-30 +(-40/5*8-2) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ))






# ret = re.search('\([^()]+\)',s)
# print(ret.group())
# ret1 = dealwithInside(ret.group())
# s = s.replace(ret.group() ,ret1).replace('+-','-')
# print(s)
# print()
#
# ret2 = re.search('\([^()]+\)',s)
# print(ret2.group())
# ret3 = dealwithInside(ret2.group())
# print(ret3)
# s = s.replace(ret2.group() ,ret3).replace('+-','-')
# print(s)

