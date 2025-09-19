def dfs(nums, target, i, j):
    if i>j:
        return -1
    m=(i+j)//2
    if nums[m]>target:
        return dfs(nums, target, i, m-1)
    elif nums[m]<target:
        return dfs(nums, target, m+1, j)
    else:
        return m
    
def BinarySearch(nums, target):
    n=len(nums)
    return dfs(nums, target, 0, n-1)


print(BinarySearch([1, 3, 4, 6, 9], 9))