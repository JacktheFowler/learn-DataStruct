"""
可以重复选取背包物品 最大价值
输入 w 物品占空间大小 v 物品价值 c 背包最大容量
输出 最大价值
动态规划 dp[i, c]=max(dp[i-1, c], dp[i, c-w[i-1]]+v[i-1]) 第i种物品容量为c时价值
i=0 dp=0 c<w[i] dp[i, c]=dp[i-1, c]
"""
def knapsackDp(w, v, c):
    n=len(w)
    dp=[[0]*(c+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for c in range(1, c+1):
            if w[i-1]>c:
                dp[i, c]=dp[i-1, c]
            else:
                dp[i, c]=max(dp[i-1][c], dp[i][c-w[i-1]]+v[i-1])
        return dp[n][c]

def knapsackDpLite(w, v, c):
    n=len(w)
    dp=[0]*(c+1)
    for i in range(1, n+1):
        for c in range(1, c+1):
            if w[i-1]>c:
                continue
            else:
                dp[c]=max(dp[c], dp[c-w[i-1]]+v[i-1])
        return dp[c]
