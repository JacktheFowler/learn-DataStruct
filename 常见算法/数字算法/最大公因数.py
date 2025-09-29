"""
gcd(a, b) a>b
if b==0 return a
a, b= b, a mod b
return gcd(a, b)
"""

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

print(gcd(9, 6))