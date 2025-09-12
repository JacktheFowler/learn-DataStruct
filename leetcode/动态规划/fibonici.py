def solve(n):
    a=[0, 1, 1]
    while True:
        if n-2>0:
            tmp=a[2]
            a[2]=a[0]+a[1]+a[2]
            a[0]=a[1]
            a[1]=tmp
            n-=1
        else:
            if n==0: 
                return a[0]
            elif n==1:
                return a[1]
            else:
                return a[2]
        
print(solve(0))