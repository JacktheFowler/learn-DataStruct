"""
大致思路

容器 记录皇后所在列 对角线的y坐标 如果查询到就跳过 递推到整个棋盘 满足条件 解决方案+1
"""
def solveNQueens(n: int):
    def generateBoard():
        board = list()
        for i in range(n):
            row[queens[i]] = "Q"
            board.append("".join(row))
            row[queens[i]] = "."
        return board

    def backtrack(row: int):
        if row == n:
            board = generateBoard()
            solutions.append(board)
        else:
            for i in range(n):
                if i in columns or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                backtrack(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)
                
    solutions = list()
    queens = [-1] * n
    columns = set()
    diagonal1 = set()
    diagonal2 = set()
    row = ["."] * n
    backtrack(0)
    return solutions
    
if __name__=='__main__':
    print(1^3)