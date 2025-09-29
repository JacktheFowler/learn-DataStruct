"""
大小变换转折v v前数组l v后数组r
若r严格递减 res=sum(v)-sum(r) res<0 |res+v| else |res-v|
否则返回-1
"""
from typing import List
def splitArray(nums: List[int]) -> int:
    v=0
    for i in range(len(nums)):
        if nums[i]>v:
            v=nums[i]
        else:
            break
    else:
        return abs(sum(nums[:-1])-nums[-1])
    tmp=v+1
    for j in range(i, len(nums)):
        if nums[j]<tmp:
            tmp=nums[j]
        else:
            return -1
    res=sum(nums[:i-1])-sum(nums[i:])
    if res<0:
        return abs(res+v)
    else:
        return abs(res-v)
    
nums=[2, 4]
print(splitArray(nums))