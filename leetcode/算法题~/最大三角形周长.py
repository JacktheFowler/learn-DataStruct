from typing import List
def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    N=len(nums)
    for i in range(N-1, 1, -1):
        if nums[i]<nums[i-1]+nums[i-2]:
            return nums[i]+nums[i-1]+nums[i-2]
    return 0

print(largestPerimeter([1, 2, 1, 10]))