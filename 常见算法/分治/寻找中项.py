"""
selelct a[1..n], k
S<v T>v v为任意选择数字
select(S, k) k<=|S|
v |S|<k<=|S|+|v|
else select(T, k-|S|-|v|)

时间复杂度O(T)=O(3/4 T)+O(n) 取期望为线性
"""
import random

def select(a, k):
    v=random.choice(a)
    S, T=[], []
    cnt=0
    for i in a:
        if i<v:
            S.append(i)
        elif i==v:
            cnt+=1
        else:
            T.append(i)
    m=len(S)
    if k<=m:
        return select(S, k)
    elif m<k<=m+cnt:
        return v
    else:
        return select(T, k-m-cnt)

a=[5, 7, 9, 1, 10]
res=select(a, 2)
print(res)