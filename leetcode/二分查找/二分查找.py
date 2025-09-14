def solve(nums, target):
    start=0
    while True:
        N=len(nums)
        if N==0:
            return start
        i=N//2
        if target==nums[i]:
            return i+start
        elif target<nums[i]:
            nums=nums[:i]
        elif target>nums[i]:
            nums=nums[i+1:]
            start+=i+1

if __name__=='__main__':
    nums = [1,3,5,6]
    target = 2
    print(solve(nums, target))