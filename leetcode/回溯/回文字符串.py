from typing import List
def partition(s: str) -> List[List[str]]:
    n = len(s)
    f = [[True] * n for _ in range(n)]

    # 字符串预处理 使用动态规划 类似状态方程
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

    ret = list()
    ans = list()
    # 判断i个串是否回文
    def dfs(i: int):
        if i == n:
            ret.append(ans[:])
            return
        
        for j in range(i, n):
            if f[i][j]:
                ans.append(s[i:j+1])
                dfs(j + 1)
                # 恢复原状
                ans.pop()
    dfs(0)
    return ret

if __name__=='__main__':
    s = "aab"
    print(partition(s))

