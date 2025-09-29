"""
modexp(a, b, N)
if b==0 return 1
z=modexp(a, b//2, N)
if b is even return z**2 mod N
else return a*z**2 mod N

time O(log^2 n)
"""
def modexp(a, b, N):
    if b==0:
        return 1
    z=modexp(a, b>>1, N)
    if z%2==0:
        return z**2%N
    else:
        return a*z**2%N
    
print(modexp(2, 10, 7))