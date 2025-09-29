"""
euclid_extend(a, b)->(x, y, d) d=ax+by d is gcd(a, b)
if b==0 return 1, 0, a
x1, y1, d=euclid_extend(b, a mod b) 1=4*25-9*11
return y1, x1-a//b*y1, d        d=bx1+(a mod b)y1=bx1+(a-a//b*b)y1=ay1+b(x1-a//by1)
"""

def euclid_extend(a, b):
    if b==0:
        return 1, 0, a
    x1, y1, d=euclid_extend(b, a%b)
    return y1, x1-a//b*y1, d

print(euclid_extend(25, 11))