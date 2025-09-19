"""
数字分解
给定不重复的数字集合 可重复选取其中的数字 使数字的和为给定目标值
I list[int] 给定数字 int 目标
O list[list] 所有组合

注意 res.append 为每次选择的副本
"""

def solve(nums, target):
    def backtrace(choices, target, state:list, res:list, start):
        if target==0:
            res.append(state.copy())
            return
        for i in range(start, len(choices)):
            if target<choices[i]:
                break
            state.append(choices[i])
            backtrace(choices, target-choices[i], state, res, i)
            state.pop()

    state=[]
    res=[]
    nums.sort()
    start=0
    backtrace(nums, target, state, res, start)
    return res

print(solve([3, 5, 4], 9))