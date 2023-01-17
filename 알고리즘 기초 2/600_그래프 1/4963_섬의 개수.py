import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
def dfs(x,y):
  board[x][y]=0
  for i in range(8):
    nx=x+dr[i]
    ny=y+dc[i]
    if 0<=nx<h and 0<=ny<w and board[nx][ny]:
      dfs(nx,ny)

while(True):
  w,h = map(int,input().split())
  if w==0 and h==0:
    break
  board = [list(map(int,input().split())) for _ in range(h)]
  cnt=0
  for i in range(h):
    for j in range(w):
      if board[i][j]:
        cnt+=1
        dfs(i,j)
  print(cnt)