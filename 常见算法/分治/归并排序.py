"""
mergeSort a[1...n]
input array
output sorted array
if n>1: merge(mergeSort(a[1..n//2]), mergeSort(a[n//2+1..n]))
else: return a

merge a[1..n] b[1..m]
input sorted arrayes
output concat array which were sorted
if n==0: return b
if m==0: return a
if a[1]<b[1]:
a[1] concat merge(a[2..n], b[1..m])
else:
b[1] concat merge(a[1..n], b[2..m])
"""
from collections import deque

def merge(a:deque, b:deque)->deque:

    if isinstance(a, int):
        a=deque([a])
    if isinstance(b, int):
        b=deque([b])

    if not a:
        return b
    if not b:
        return a
    
    if a[0]<b[0]:
        p=a.popleft()
    else:
        p=b.popleft()
    q=merge(a, b)
    q.appendleft(p)
    return q
    
def queueSort(a:deque)->deque:
    while len(a)>1:
        a.append(merge(a.popleft(), a.popleft()))
    return a

print(queueSort(deque([2, 0, 7, 4, 6, 1])))