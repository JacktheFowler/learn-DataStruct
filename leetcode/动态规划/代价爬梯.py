"""
输入 爬梯子代价列表
输出 最小代价

指针 i
局部最优 

注意到顶
"""

def solve(cost):
    i=-1
    c=0
    N=len(cost)
    while i<N-1:
        if cost[i+1]<cost[i+2]:
            c+=cost[i+1]
            i+=1
        else:
            c+=cost[i+2]
            i+=2
    return c

cost = [1,100,1,1,1,100,1,1,100,1]
print(solve(cost))