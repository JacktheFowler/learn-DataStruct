"""
满二叉树搜索
左>根>右
构造树， 查询

I
满二叉搜索树 2**n-1 1<=n<=10
待查询数 -32768~32767 i4
O
搜索顺序 S根 R 右子树 L左子树 Y找到 N未找到
1 2 3 4 5 6 7
搜索树
     4
   6   2
  7 5 3  1
"""

# 等待

import sys
sys.stdin=open('summer_24_4_24/1.1')
def input_data():
    data=[int(i) for i in  sys.stdin.readline().split()]
    data.sort()
    search=int(sys.stdin.readline())
    return data, search

# (i 列表 o 搜索满二叉树)
def search_tree(data):
    N=len(data)
    if N==0:
        return data
    idx=int(N//2)
    root=data[idx]
    left_child=search_tree(data[:idx])
    right_child=search_tree(data[idx+1:])
    return [root]+right_child+left_child



def solve():
    data, search=input_data()
    tree=search_tree(data)
    print(tree)

solve()