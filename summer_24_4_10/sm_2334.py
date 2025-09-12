# 相似度
# 给定相似度矩阵 间接相似度 不计 相似计入一个集合
# 输入
# r1 矩阵形状
# rn 相似度矩阵
# 输出
# 由大到小集合相似度
# 解法 更新类 和 集合相似度
#  间接相似是烟幕弹
import sys

def input_data():
    N=int(sys.stdin.readline())
    mat=[]
    for _ in range(N):
        data=[int(i) for i in sys.stdin.readline().split()]
        mat.append(data)
    return mat


