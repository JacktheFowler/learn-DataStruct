"""
给定i个物品，第i个物品的重量为w[i-1]、价值为v[i-1]，和一个容量为c的背包。每个物品只能选择一次，问在限定背包容量下能放入物品的最大价值。
暴力搜索 和动态规划
"""

# 暴力搜索 自顶至底
def knapsackDfs(w, v, i, c):
    if i==0 or c==0:
        return 0
    if w[i-1]>c:
        return knapsackDfs(w, v, i-1, c)
    yes=knapsackDfs(w, v, i-1, c-w[i-1])+v[i-1]
    no=knapsackDfs(w, v, i-1, c)
    return max(yes, no)

# 动态规划 填充dp表 dp[i][w]->v
def knapsackDp(w, v, c):
    n=len(w)
    dp=[[0]*(c+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for c in range(1, c+1):
            if w[i-1]>c:
                dp[i][c]=dp[i-1][c]
            else:
                dp[i][c]=max(dp[i-1][c], dp[i-1][c-w[i-1]]+v[i-1])
    return dp[n][c]

# 转移状态只与上一行状态有关 使用倒序遍历 防止容量小的状态被覆盖
def knapsackDpComp(w, v, c):
    n=len(w)
    dp=[0]*(c+1)
    for i in range(1, n+1):
        for c in range(c+1, 1, -1):
            if w[i-1]>c:
                continue
            else:
                dp[c]=max(dp[c], dp[c-w[i-1]]+v[i-1])
    return dp[c]