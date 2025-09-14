"""
set 省节点
idx 省对应 集合编号
检查邻接矩阵 如果不存在集合 创建 否则加入
"""
def solve(isConnected):
    d={}
    idx=[0]*len(isConnected)
    for i, j in enumerate(isConnected):
        if i not in d:
            d[i]=set()
        for k, h in enumerate(j):
            d[i].update(h)
            idx[k]=i

if __name__=='__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    