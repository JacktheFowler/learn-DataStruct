"""
n-bit positive multiply
mul x, y -> z
x y n bits positive integers
z products
if n==1 return xy
xl xr= leftmost n/2 rightmost n//2 bits of x
yl yr= leftmost n/2 rightmost n//2 bits of y
P1=mul(xl, yl)
P2=mul(xr, yr)
P3=mul(xl+xr, yl+yr)
return P1*2**n+(P3-P1-P2)*(2**n/2)+P2
"""

# obtain right half and left half bits
def bit_process(x:int):
    N=x.bit_length()
    mask_right=(1<<(N//2))-1
    mask_left=(1<<N)-(1<<N//2)
    l=(x&mask_left)>>(N//2)
    r=x&mask_right
    return l, r, N
