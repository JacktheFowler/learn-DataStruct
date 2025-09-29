"""
div x, y-> q, r
if x==0 q, r=0, 0
q, r=div(x//2, y)
r->2r q->2q
x is odd r->r+1
r>=y q->q+1 r->r-y
"""

def div(x, y):
    if x==0:
        return 0, 0
    q, r=div(x>>1, y)
    q, r=q<<1, r<<1
    if x%2==1:
        r+=1
    if r>=y:
        q+=1
        r-=y
    return q, r

print(div(5, 3))