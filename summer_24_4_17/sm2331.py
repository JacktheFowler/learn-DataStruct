"""
云上服务-树的遍历

统计 DI值 DI=5*严重问题+2*一般问题 DI>阈值为危险服务

I
r1 M <100_000云服务阈值 N 1000统计数据行数
r2~rN+1 c1 服务节点 c2服务父节点 c3 问题级别 0为严重 1为一般 c4问题数量

O
风险服务个数 int
"""
import sys
from collections import defaultdict
def input_data():
    M, N=[int(i) for i in sys.stdin.readline().split()]
    work=defaultdict(lambda: {'child': '', 'level': '', 'num': 0})
    for _ in range(N):
        data=sys.stdin.readline().split()
        child, parent, level, num=data[0], data[1], data[2], int(data[3])
        work[parent]['child']=child
        work[parent]['level']=level
        work[parent]['num']=num
    return M, work

def work_tree(work):
    res=defaultdict(list)
    res[0]='*'
    stack=['*']
    i=0
    while stack:
        parent=stack.pop()
        item=work.get(parent)
        if item is None:
            return res
        else:
            i+=1
            res[i].append(item['child'])
            stack.extend(item['child'])

    return res

def solve():
    M, work=input_data()
    res=work_tree(work)

    return res

print(solve())
