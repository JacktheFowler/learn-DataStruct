"""
24点游戏
使用回溯 perm(4, 2)*4perm(3, 2)*4perm(2, 2)*4{算符类型}=12*6*2*4*3=9216
state 改变 是choice  
结束递归条件 state=[] False state[0]-target<eps 返回True
终止本轮条件 上轮True 

注意 
判断相等可能出现浮点数 除数出现0情况 eps 
+ *顺序不敏感 可跳过「剪枝」
"""
def solve(cards):
    TARGET=24
    ADD, MUL, SUB, DIV=0, 1, 2, 3
    eps=1e-6
    def backtrace(state:list):
        if state==[]:
            return False
        if state[0]-TARGET<eps:
            return True
        for i, x in enumerate(state):
            for j, y in enumerate(state):
                if i!=y:
                    newList=list()
                for k, z in enumerate(state):
                    if k!=i and k!=j:
                        newList.append(k)
                for k in range(4):
                    if i>j and k<2:
                        continue
                    if k==ADD:
                        newList.append(i+j)
                    if k==MUL:
                        newList.append(i*j)
                    if k==SUB:
                        newList.append(i-j)
                    if k==DIV:
                        if j<eps:
                            continue
                        newList.append(i/j)
                    if solve(newList):
                        return True
                    newList.pop()
        return False
    return backtrace(cards)

print(solve([1, 2, 3, 4]))

        