import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

group = {}

def bfs(g,start_x,start_y):
  cnt=1
  board[start_x][start_y]=-1
  visited[start_x][start_y]=g
  q = deque([(start_x,start_y)])
  while q:
    x,y= q.popleft()
    for i in range(4):
      nx = x+dr[i]
      ny = y+dc[i]
      if 0<=nx<n and 0<=ny<m and not board[nx][ny] and not visited[nx][ny]:
        board[nx][ny]=-1
        visited[nx][ny]=g
        q.append((nx,ny))
        cnt+=1
  group[g]=cnt

g=1

visited=[[0 for j in range(m)] for i in range(n)]

for i in range(n):
  for j in range(m):
    if not board[i][j]:
      bfs(g,i,j)
      g+=1

for i in range(n):
  for j in range(m):
    if board[i][j]==1:
      check=set()
      for k in range(4):
        ni = i+dr[k]
        nj = j+dc[k]
        if 0<=ni<n and 0<=nj<m and visited[ni][nj]:
          check.add(visited[ni][nj])
      for ch in check:
        board[i][j]+=group[ch]
      board[i][j]%=10
    else:
      board[i][j]=0


for b in board:
  print("".join(map(str,b)))