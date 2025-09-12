"""
扑克游戏
连续三张卡牌消去 最终无卡牌是 返回0

I
扑克数量 N 1~52
卡牌序列 2-10 A J Q K
O
消去卡牌
"""

import sys

def input_data():
    N=int(sys.stdin.readline())
    card=list(sys.stdin.readline().split())[:N]
    return N, card

def process_poker(card):
    N=len(card)
    for i in range(N-2):
        if card[i]==card[i+1]==card[i+2]:
            break
    else:
        return card
    # 对于存在三张相同的卡牌
    card=card[:i]+card[i+3:]
    if card:
        return card
    else:
        return [0]

def solve():
    N, card=input_data()
    while True:
        res=process_poker(card)
        if res==card or res==0:
            return res
        else:
            # 更新牌
            card=res

card=solve()
for i in card:
    print(i, sep=' ')
