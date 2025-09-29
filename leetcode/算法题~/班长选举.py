"""
r1 n m 选举轮数 对手每轮或得票数
r2~rn+1 每轮选择获得票数 ai bi ci {ai整个选举仅能选择一次}
输出 最大票数差

dp[0][i]=max(dp[0])+ch[i] dp[1][i]=max(dp[1])+ch[i] i=1, 2
dp[1][0]=max(dp[0])+ch[0] 
"""

import sys
sys.stdin=open('leetcode/算法题/班长选举.txt')
dp=[[0]*3 for _ in range(2)]
n, m=[int(i) for i in sys.stdin.readline().split(',')]
for _ in range(n):
    ch=[int(i) for i in sys.stdin.readline().split(',')]
    p, q=max(dp[0]), max(dp[1])
    dp[1][0]=p+ch[0]
    for i in range(1, 3):
        dp[0][i]=p+ch[i]
        dp[1][i]=q+ch[i]

p, q=max(dp[0]), max(dp[1])
res=max(p, q)-m*n
if res<0:
    print('no')
else:
    print('yes')
print(abs(res))