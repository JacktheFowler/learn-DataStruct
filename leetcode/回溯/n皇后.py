"""
按行扫描 choice 每列 停止条件 row==n 回退条件 diag1..已存在 尝试append(col) 进行下一轮选择
diag1[col]=row-col diag2[col]=row+col cols[list]
合理使用全局变量
"""
def mySolve(n):
    def generateBoard(state):
        board=[]
        for i in state:
            row[i]='Q'
            board.append(''.join(row))
            row[i]='.'
        return board

    def backtrace(row:int):
        if row==n:
            board=generateBoard(state)
            res.append(board)
        else:
            for col in range(n):
                diag1=row-col
                diag2=row+col
                if col in cols or diag1 in diag1s or diag2 in diag2s:
                    continue
                cols.add(col)
                diag1s.add(diag1)
                diag2s.add(diag2)
                state.append(col)
                backtrace(row+1)
                cols.remove(col)
                diag1s.remove(diag1)
                diag2s.remove(diag2)
                state.pop()
    
    row=['.']*n
    state=[]
    res=[]
    diag1s=set()
    diag2s=set()
    cols=set()
    backtrace(0)
    return res

print(mySolve(4))


