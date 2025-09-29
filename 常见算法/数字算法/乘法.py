"""
mul x, y
if y==0 return 0
z=mul(x, y//2)
if y is even return 2*z
if y is odd return 2*z+x
<< or >> has lower operate level than others
time O(n^2) n is max bit length of (x, y)
"""

def mul(x, y):
    if y==0:
        return 0
    z=mul(x, y>>1)
    if y%2==0:
        return z<<1
    else:
        return (z<<1)+x
    
print(mul(3, 5))
