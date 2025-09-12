# 循环依赖
# 只存在唯一循环依赖
# 输入
# N 关系数
# 所有关系 格式为 依赖个数 0 元素编号 1 依赖元素 :
# 3_1 1 2 3 1
# 想法 列表收集依赖关系 dfs遍历可以找到key返回依赖 
import sys

def input_relation():
    data=sys.stdin.readlines()
    num_relation=int(data[0])
    rely_dict={}
    for idx in range(num_relation):
        line=data[idx+1]
        num, elem, *rely=[int(i) for i in line.split()]
        rely=rely[:num-1]
        rely_dict[elem]=rely

    return rely_dict

def rely_circ(rely_dict, key, collect=None):
    if collect is None:
        collect=[key]
    for item in rely_dict[key]:
        if item in rely_dict.keys():
            if item in collect:
                idx=collect.index(item)
                collect=collect[idx:]
                collect.append(item)
                return collect
            else:
                collect.append(item)
                return rely_circ(rely_dict, item, collect)
    else:
        return None

def solve():
    rely_dict=input_relation()
    for k in rely_dict:
        res=rely_circ(rely_dict, k)
        if res:
            return res

print(solve())
