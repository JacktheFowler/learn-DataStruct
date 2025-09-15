card=[1, 0, 3, 4]
# 将列表数字拆分为二元组 更新二元组的所有可能结果
def process(card):
    a=[card[0]+card[1], card[0]-card[1], card[1]-card[0], card[0]*card[1]]
    if 0 in card:
        a.append(0)
    else:
        a.extend([card[0]/card[1], card[1]/card[0]])
    return a

def solve(card):
    d={}
    for i in range(1, len(card)):
        key=(card[0], card[i])
        if key not in d:
            d[key]=process(key)
        # else:

if __name__=='__main__':
    print(process(card))