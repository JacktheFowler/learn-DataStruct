# 37 数独

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
    chess=[[[], [], []], 
           [[], [], []], 
           [[], [], []]]
    r=[[] for _ in range(9)]
    c=[[] for _ in range(9)]
    p=set('123456789')
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item.isdigit():
                chess[i//3][j//3].append(item)
                r[i].append(item)
                c[j].append(item)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='.':
                adj=set()
                adj.update(chess[i//3][j//3], r[i], c[j])
                t=p-adj
                # yy
                while t:
                    # a为尝试
                    a=t.pop()
                    r[i].append(a)
                    c[j].append(a)
                    chess[i//3][j//3].append(a)
                    

if __name__=='__main__':
    res=input_data(board)
    pprint(res)

