import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]


s=0
safe=[]
virus=[]
for i in range(n):
  for j in range(m):
    if board[i][j]==0:
      s+=1
      safe.append((i,j))
    elif board[i][j]==2:
      virus.append((i,j))
      

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def bfs(next_board):
  q = deque(virus)
  # 바이러스 갯수
  cnt=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<m and not next_board[nx][ny]:
        next_board[nx][ny]=2
        cnt+=1
        q.append((nx,ny))
  return cnt

ans=0
for ((n1x,n1y),(n2x,n2y),(n3x,n3y)) in combinations(safe,3):
  next_board=[row[:] for row in board]
  next_board[n1x][n1y]=1
  next_board[n2x][n2y]=1
  next_board[n3x][n3y]=1
  ns=bfs(next_board)
  # safe 구역, ns 바이러스가 퍼진 구역, -3 벽 3칸
  ans = max(ans,s-ns-3)
print(ans)