"""

问题
找出最大的内聚环 内聚值H=L-V L为环大小 V为接口数
I
r1 服务数
r2 服务关系
O
最大内聚环 从最小编号开始
"""

import sys
sys.stdin=open('summer_24_4_24/3.1')
def input_data():
    N=int(sys.stdin.readline())
    relation=[(i, j) for i, j in 
              enumerate(sys.stdin.readline().split())][:N]
    return relation

if __name__=='__main__':
    relation=input_data()
    print(relation)