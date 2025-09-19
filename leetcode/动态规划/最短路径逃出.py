"""
给定一个m*n的二维网格 grid ，网格中的每个单元格包含一个非负整数，表示该单元格的代价。
机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达右下角单元格。请返回从左上角到右下角的最小路径和。

下使用暴力搜索 动态规划「清晰版 空间优化版」 
使用表记录每个歌格子的可能最短路径 路径只往下或往右

"""
from math import inf
# 暴力搜索并记忆化
def minPathDfs(grid):
    def dfs(grid, i, j, mem):
        if i==j==0:
            return grid[0][0]
        if i<0 or j<0:
            return inf
        # 记忆已尝试过的最短子路径
        if mem[i][j]!=-1:
            return mem[i][j]
        left=dfs(grid, i-1, j)
        up=dfs(grid, i, j-1)
        mem[i][j]=min(left, up)+grid[i][j]
        return mem[i][j]
    i, j=len(grid), len(grid[0])
    mem=[[-1]*j for _ in range(i)]
    return dfs(grid, i, j, mem)

# 动态规划 dp[i, j]=min(dp[i-1, j], dp[i, j-1])+grid[i][j] 但从最小问题开始
# 对于首行仅可能由首行转移
def minPath(grid):
    n, m=len(grid), len(grid[0])
    dp=[[0]*m for _ in range(n)]
    # 首行
    dp[0][0]=grid[0][0]
    for i in range(1, m):
        dp[0][i]=dp[0][i-1]+grid[0][i]
    # 首列
    for i in range(1, n):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    # 逐网格转移
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
    return dp[n-1][m-1]

# 动态规划 空间优化 对列扫描
def minPathComp(grid):
    n, m=len(grid), len(grid[0])
    dp=[0]*m
    dp[0]=grid[0][0]
    for i in range(1, m):
        dp[i]=dp[i-1]+grid[0][i]

    for i in range(1, n):
        dp[0]=dp[0]+grid[i][0]
        for j in range(1, n):
            dp[j]=min(dp[j-1], dp[j])+grid[i][j]
    return dp[m-1]
