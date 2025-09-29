"""
process 
parameter num
var l存储结果 需反向 tmp=0 i=1存储余数
if tmp==n: return l[::-1]
m=10^i%a
if m!=tmp: insert m-tmp to l; tmp=m
i+=1
"""

from typing import List
def decimalRepresentation(n: int) -> List[int]:
        tmp, i=0, 1
        l=[]
        while True:
                if tmp==n:
                        return l[::-1]
                m=n%(10**i)
                if m!=tmp:
                        l.append(m-tmp)
                        tmp=m
                i+=1

print(decimalRepresentation(102))