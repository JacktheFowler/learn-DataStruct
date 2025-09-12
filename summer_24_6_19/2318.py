"""
依赖关系

I
r1 n 模块数
r 2~n+1 c1 Ki 模块i依赖数量 c 2~Ki+1 依赖
O
构建次数
"""
import sys
sys.stdin=open('summer_24_6_19/1.1')

def input_data():
    n=int(sys.stdin.readline())
    mode={}
    for i in range(n):
        data=[int(i) for i in  sys.stdin.readline().split()]
        K=data[0]
        if K==0:
            mode[i+1]=0
        else:
            mode[i+1]=data[1:K+1]
    return n, mode

# 输入 构建好模块 返回 可构建模块
def construct(mode, now):
    res=[]
    for i in mode:
        if mode[i] in now:
            res.append(i)
        elif mode[i]==0 and (i not in now):
            res.append(i)
    return res
        
def solve():
    n, mode=input_data()
    res=[]
    cnt=0
    while True:
        new=construct(mode, res)
        if new:
            res.extend(new)
            cnt+=1
        else:
            return -1
        if len(res)==n:
            return cnt

if __name__=='__main__':
    # print(solve())
    n, mode=input_data()
    new=construct(mode, [5])
    print(new)