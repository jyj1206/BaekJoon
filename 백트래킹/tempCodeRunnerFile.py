import sys
input = sys.stdin.readline
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))

solve=[]
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            solve.append([i,j])

def promising(i):
    s_r, s_c=solve[0][0],solve[0][1]
    # 행 비교
    if i in sudoku[s_r]:
        return False
    # 열 비교
    for j in range(9):
        if i == sudoku[j][s_c]:
            return False
    # 9칸 비교
    for j in range(s_r//3*3,s_r//3*3+3):
        for k in range(s_c//3*3,s_c//3*3+3):
            if i==sudoku[j][k]:
                return False
    return True 

def solve_sudoku():
    if len(solve)==0:
        for i in sudoku:
            print(' '.join(map(str,i)))
        return
    for i in range(1,10):
        if promising(i):
            a,b=solve[0][0],solve[0][1]
            sudoku[a][b]=i
            solve.pop(0)
            solve_sudoku()
            solve.insert(0,[a,b])
            sudoku[a][b]=0

solve_sudoku()