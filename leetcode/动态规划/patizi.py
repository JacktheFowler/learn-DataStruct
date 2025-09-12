# 爬楼梯 每次爬1 或2 爬几次
def solve(n):
    a=[1, 2]
    while True:
        if n>len(a):
            a.append(a[-1]+a[-2])
        else:
            return a[n-1]

print(solve(1))

# 变种 给定i(0~n)阶楼梯花销cost[i] 可爬1或2 求最小花销
# I cost = [1,100,1,1,1,100,1,1,100,1] O 6