# 计费
# 输入
# 1 日志数量 1~1000
# 2~n+1 日志 4列
    # c1 时间戳 str10[int] 同一时间 计费一次 先到先得
    # c2 客户标示 str<16 
    # c3 计费因子 str<16 如果查询不到 计费单价0 
    # c4 计费时长 0~100 超出计0
# n+2 计费因子数量 m 1~100
# n+3~n+3+m 计费单价列表
# c1 计费因子 str<16 c2 单价 uint 1~100
# c1 客户名 c2 话费 按字典升序
# 输出 1_1 client1= 15x5+8x7=131
# client2= 0x5+35x7=245
import sys
from collections import defaultdict
def input_log():
    log={}
    num_log=int(sys.stdin.readline())
    for _ in range(num_log):
        time, client, factor, duration=sys.stdin.readline().split(',')
        duration=int(duration)
        if time not in log:
            log[time]={
                'client':client, 
                'factor':factor, 
                'duration':duration}
            
    num_factor=int(sys.stdin.readline())
    factor={}
    for _ in range(num_factor):
        client, pay=sys.stdin.readline().split(',')
        factor[client]=int(pay)

    return log, factor

def solve():
    log, factor=input_log()
    res=defaultdict(int)
    for v in log.values():
        res[v['client']]+=v['duration']*factor.get(v['factor'], 0)
    return res

res=solve()
for k, v in res.items():
    print(f'{k},{v}')
