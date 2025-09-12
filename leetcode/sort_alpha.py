import sys
# 对元音排序 辅音不变

def input_data():
    return sys.stdin.readline()

# 容器 a alpha n idx 映射排序 替换
def sort_alpha(data):
    target='aeiouAEIOU'
    a=[]
    n=[]
    data=list(data)
    for i, j in enumerate(data):
        if j in target:
            a.append(j)
            n.append(i)

    new=sorted(a)
    for i in range(len(a)):
        data[n[i]]=new[i]
    return ''.join(data)

if __name__=='__main__':
    data=input_data()
    res=sort_alpha(data)
    print(res)