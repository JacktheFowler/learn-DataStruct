# 最大长度相当 但更小的替换 
# 当新数字 大于较小的 小于较大的 替换较大的 长度不变
# 对于 小于较小的 开辟新空间 计数
def solve(nums):
    p=0
    # a<b
    a=b=-9000
    q=[]
    for i in nums:
        if i>b:
            p+=1
            a=b
            b=i
        elif a<i<b:
            b=i
    return p

if __name__=='__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(solve(nums))