"""
格雷码 是 首位为0 相邻仅有一位不同 最后一位与首位相邻的编码
输入 格雷码位数 输出 所有格雷码序列

思考 已知n-1为格雷码G 只需将G翻转 并置首位 连接即可
"""
from typing import List
def grayCode(n: int) -> List[int]:
    ans = [0]
    for i in range(1, n + 1):
        for j in range(len(ans) - 1, -1, -1):
            ans.append(ans[j] | (1 << (i - 1)))
    return ans

print(grayCode(4))