"""
输入两个字符串 s 和 t ，返回将 s 转换为 t 所需的最少编辑步数。
你可以在一个字符串中进行三种编辑操作：插入一个字符、删除一个字符、将字符替换为任意一个字符。

使用动态规划 dp[i, j]=min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])+1 分别表示删除 增加 修改 更新方向为左上
s[i]==s[j] dp[i, j]=dp[i-1, j-1] 字符相等
dp[0, j]=j dp[i, 0]=i 临界状态
"""
def edit_distance(s, t):
    n, m=len(s), len(t)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0]=i
    for j in range(1, m+1):
        dp[0][j]=j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    return dp[n][m]

def editDistanceLite(s, t):
    n, m=len(s), len(t)
    dp=[0]*(m+1)
    for j in range(1, m+1):
        dp[j]=j
    for i in range(1, n+1):
        leftup=dp[0]
        dp[0]+=1
        for j in range(1, m+1):
            tmp=dp[j]
            if s[i-1]==t[j-1]:
                dp[j]=leftup
            else:
                dp[j]=min(dp[j], dp[i][j-1], leftup)+1
            leftup=tmp
    return dp[m]