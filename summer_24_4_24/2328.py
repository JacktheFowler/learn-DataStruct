"""
进球

规则
进球数多
最多连续进球数量
第一次失手的
编号小的

I
r1 球员数n 射门数2**n-1
r2 射门情况 1 入 0 失
O
射门能力 由强到弱
"""

import sys
sys.stdin=open('summer_24_4_24/2.1')

def input_data():
    n, m=[int(i) for i in sys.stdin.readline().split()]
    score=[[int(i) for i in line] for line in sys.stdin.readline().split()]
    return n, m, score



print([0, 0, 1, 1, 1].index())
# solve()