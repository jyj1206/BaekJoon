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

def promising(i,idx):
    s_r, s_c=solve[idx][0],solve[idx][1]
    nx,ny=s_r//3*3,s_c//3*3
    # 행 비교
    if i in sudoku[s_r]:
        return False
    # 열 비교
    for j in range(9):
        if i == sudoku[j][s_c]:
            return False
    # 9칸 비교
    for j in range(3):
        for k in range(3):
            if i==sudoku[j+nx][k+ny]:
                return False
    return True 

def solve_sudoku(idx):
    if idx==len(solve):
        for i in range(9):
            print(*sudoku[i])
        exit(0)   
    for i in range(1,10):
        a,b=solve[idx][0],solve[idx][1]
        if promising(i,idx):
            sudoku[a][b]=i
            solve_sudoku(idx+1)
            sudoku[a][b]=0

solve_sudoku(0)