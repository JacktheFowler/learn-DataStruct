"""
set 省节点
idx 省对应 集合编号
检查邻接矩阵 如果不存在集合 创建 否则加入 选择merge已有集合
"""
def solve(isConnected):
    N=len(isConnected)
    d=[[] for _ in range(N)]
    h=[]
    idx=[0]*N
    cnt=0
    for i, j in enumerate(isConnected):
        if idx[i]==0:
            cnt+=1
            idx[i]=cnt
        for p, k in enumerate(j):
            if k==1:
                if p not in d[idx[i]-1]:
                    d[idx[i]-1].append(p)
                    h.append(p)
                    idx[p]=cnt
    return cnt
        


if __name__=='__main__':
    isConnected=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(solve(isConnected))
    