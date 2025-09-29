def climbStairBacktrace(n):
    def backtrace(n, state, choices, res):
        if state==n:
            res[0]+=1

        for choice in choices:
            state+=choice
            if state>n:
                continue
            backtrace(n, state, choices, res)
    res=[0]
    state=0
    choices=[1, 2]
    backtrace(n, state, choices, res)
    return res[0]

# 最小代价爬梯 最小花费 dp[i]=min(dp[i-1], dp[i-2])+cost[i]
def climb_cost(cost):
    n=len(cost)
    if n==1 or n==2:
        return cost[n-1]
    a, b=cost[0], cost[1]
    for i in range(2, n):
        a, b=b, min(a, b)+cost[i]
    return b

# 约束条件爬梯 规定不能连续跳1阶
# dp[i, j] 为在第i阶 上次跳跃为j dp[i, 1]=dp[i-1, 2] dp[i, 2]=dp[i-2, 1] + dp[i-2, 2]
def climb_cond(n):
    if n==1 or n==2:
        return 1
    dp=[[0]*3 for _ in range(n+1)]
    dp[1][1], dp[1][2]=1, 0
    dp[2][1], dp[2][2]=0, 1
    for i in range(3, n+1):
        dp[i][1]=dp[i-1][2]
        dp[i][2]=dp[i-2][1]+dp[i-2][2]
    return dp[n][1]+dp[n][2]

# 动态规划dp表