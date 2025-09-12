def solve(a):
    n1=sum(a[::2])
    n2=sum(a[1::2])
    if n1<n2:
        return n1
    else:
        return n2
    
# 3, 1, 1, 7]