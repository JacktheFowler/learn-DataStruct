def permutation(nums):
    def backtrace(choices, selects, states, res):
        if len(choices)==len(selects):
            # 注意列表的可变性
            res.append(selects.copy())
            return
        duplicated = set[int]()
        for i, choice in enumerate(choices):
            if not states[i] and choice not in duplicated:
                selects.append(choice)
                duplicated.add(choice)
                states[i]=True
                backtrace(choices, selects, states, res)
                states[i]=False
                selects.pop()
    states=[False]*len(nums)
    res=[]
    backtrace(nums, [], states, res)
    return res
