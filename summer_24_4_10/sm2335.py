"""
公网下线
mat[i][j]=p表示节点i到节点j所需权限 0为禁止通过 访问后j权限为p
exposed数组为暴露的公网节点 黑客入侵 得到root 10权限 国际节点数为R
使R最小

输入
r1 网络节点数量 2<=N<=24
r2~rn+1 权限 0<=v<=10
: 暴露公网节点 0<=exposed<=N-1

输出
下线端口号 多个节点返回索引最小的

样例
I 2335_1 O 3
"""

"""
问题实质 就是从哪个公网节点进入会感染尽可能多的节点 
类似传染病
忽略权限发生变化这一条件 :(
"""

"""
对于递归 函数参数每次调用发生变化 对于需要少量参数的应用符合
对于stack 则需要设计结果容器 和 记录容器stack
"""
import sys

def input_data():
    N=int(sys.stdin.readline())
    mat=[]
    for _ in range(N):
        data=[int(i) for i in sys.stdin.readline().split()]
        mat.append(data)
    exposed_data=[int(i) for i in sys.stdin.readline().split()]
    sys.stdin.close()
    return mat, exposed_data

# 使用dfs解决
def find_point(mat, point):
    access=10
    res=[point]
    stack=[point]
    N=len(mat)
    while stack:
        p=stack.pop()
        for i in range(N):
            if 0<mat[p][i]<=access and (i not in res):
                res.append(i)
                stack.append(i)
                access=mat[p][i]
    return res
# 对字典排序 key默认对键值应用
def solve():
    mat, exposed_data=input_data()
    res={}
    for i in exposed_data:
        res[i]=find_point(mat, i)
    res=max(res, key=lambda i: len(res[i]))
    return res

print(solve())
