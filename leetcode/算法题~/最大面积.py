"""
S=abs(ad-bc)/2 a=x1-x2 b=y1-y2 c=x3-x2 d=y3-y2

"""

from typing import List
from itertools import combinations

def largestTriangleArea(points: List[List[int]]) -> float:
    def area(points):
        a=points[0][0]-points[1][0]
        b=points[0][1]-points[1][1]
        c=points[2][0]-points[1][0]
        d=points[2][1]-points[1][1]
        return abs(a*d-b*c)/2
    
    pick=combinations(points, 3)
    MAX=0
    for point in pick:
        a=area(point)
        if a>MAX:
            MAX=a
    return MAX

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(largestTriangleArea(points))