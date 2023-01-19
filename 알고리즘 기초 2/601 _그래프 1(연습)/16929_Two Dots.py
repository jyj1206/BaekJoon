import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m =map(int,input().split())

board=[]
visited=[[0 for i in range(m)] for j in range(n)]

for i in range(n):
  board.append(list(input().strip()))
  
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def dfs(prev_x,prev_y,x,y):
  visited[x][y]=1
  for i in range(4):
    nx=x+dr[i]
    ny=y+dc[i]
    if 0<=nx<n and 0<=ny<m and board[nx][ny] == board[x][y]:
      if not visited[nx][ny]:
        cycle=dfs(x,y,nx,ny)
        if cycle:
          return True
      elif prev_x!=None and prev_y!=None:
        if prev_x!=nx or prev_y!=ny:
          return True
  return False


def solution():
  for i in range(n):
    for j in range(m):
      if not visited[i][j]:
        cycle=dfs(None,None,i,j)
        if cycle:
          return True
  return False
print('Yes' if solution() else 'No')

