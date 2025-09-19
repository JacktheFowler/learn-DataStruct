"""
选择回溯
当选择pos==len(space) 无空白结束 flag=True
选择 1~9 剪枝 不在同一3*3 row col 当找到解 flag结束递归

"""
from pprint import pprint
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
# 处理棋盘 返回九宫格数字 3x3
def input_data(board):
    space=[]
    block=[[[False]*9 for _ in range(3)] for _ in range(3)]
    row=[[False]*9 for i in range(9)]
    col=[[False]*9 for i in range(9)]
    flag=False

    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                space.append((i, j))
            else:
                digit=int(board[i][j])-1
                row[i][digit]=col[digit][j]=block[i//3][j//3][digit]=True
    def backtrace(pos):
        nonlocal flag
        if pos==len(space):
            flag=True
            return
        x, y=space[pos]
        for digit in range(9):
                if row[x][digit] or col[digit][y] or block[x//3][y//3][digit]:
                    continue
                row[x][digit]=col[digit][y]=block[x//3][y//3][digit]=True
                board[x][y]=str(digit+1)
                backtrace(pos+1)
                row[x][digit]=col[digit][y]=block[x//3][y//3][digit]=False
                if flag:
                    return
    backtrace(0)

                    

if __name__=='__main__':
    input_data(board)
    pprint(board)

