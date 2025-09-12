# 积木游戏
# 塔顶数字等于下面连续数字之和即可消去
# 输入 积木塔数字 数字范围 1~2^32-1(unsigned int) 个数 1~1000
# 输出 10 242

import sys

def input_args():
    data=sys.stdin.read().split()
    return [int(i) for i in data]

def merge(tower):
    for i, num in enumerate(tower):
        sum=0
        for j in range(i):
            sum+=tower[i-1-j]
            if num==sum:
                new = num*2
                new_tower=tower[0:i-1-j]+[new]+tower[i+1:]
                return new_tower
    else:
        return tower
    
def final_tower(tower):
    while True:
        new_tower=merge(tower)
        if new_tower==tower:
            return new_tower[::-1]
        else:
            tower=new_tower

def solve():
    tower=input_args()
    return final_tower(tower)

print(solve())