# 对车上乘客按终点站排序 终点站靠前topn有座位
# 输入 
# 列车座位数量 1<=m<=9 停靠站点数量 2<=n<=20 预订乘客数 1<=x<=9
# x行输入 上车站点 下车站点
# 1_1 19 2_1 10
# 我的解法 站点车上人数 计数 少于座位数的站点
# 注意 end站不计
import sys
# sys.stdin=open('summer_24_3_20/1_1')
def solve():
    data=sys.stdin.readlines()
    seats, stations, members=[int(i) for i  in data[0].split()]
    bus=[0]*stations

    for line in range(members):
        line=data[line+1]
        start, end=[int(i) for i in line.split()]
        bus[start]+=1
        if end-start>1:
            bus[end-1]+=1

    tmp=bus[::-1]
    for i in range(len(tmp)):
        bus[i]=sum(tmp[:i+1])
    
    res=map(lambda a: seats if a>seats else a, bus)

    return sum(res)

print(solve())