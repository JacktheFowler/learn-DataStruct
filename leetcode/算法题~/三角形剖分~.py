from typing import List


def minScoreTriangulation(values: List[int]) -> int:
    values.sort()
    tmp=0
    for i in range(2, len(values)):
        tmp+=values[0]*values[1]*values[i]
    return tmp

print(minScoreTriangulation([1, 3, 1, 4, 1, 5]))
        