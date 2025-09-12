"""
模式匹配

匹配次数 转化为匹配类型 进行统一匹配
I
正则' 表达式
O
匹配内容 未匹配输出!
"""

import sys
sys.stdin=open('summer_24_5_8/2.2')
def input_data():
    re=sys.stdin.readline()
    string=sys.stdin.readline()
    return re, string

def re_mean(re):
    typ=[]
    num=[]
    weight=[]
    res=[]
    w=1
    for i in re:
        if i.isdigit():
            w=int(i)*w
            num.append(int(i))
        if i==')':
            w/=num.pop()
        elif i in 'A' or i in 'N':
            typ.append(i)
            weight.append(w)

    for i in range(len(typ)):
        res.append(typ[i]*weight[i])

    return ''.join(res)


if __name__=='__main__':
    re, string=input_data()
    print(re_mean(re))
        
