import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)
from collections import deque
t = int(input())

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def bfs(start_x,start_y):
  queue=deque([(start_x,start_y)])
  field[start_x][start_y]=0
  while queue:
    cur_x,cur_y=queue.popleft()
    for i in range(4):
      nx=cur_x+dr[i]
      ny=cur_y+dc[i]
      if 0<=nx<n and 0<=ny<m and field[nx][ny]==1:
        queue.append((nx,ny))
        field[nx][ny]=0

# def dfs(cur_x,cur_y):
#   field[cur_x][cur_y]=0
#   for i in range(4):
#     nx=cur_x+dr[i]
#     ny=cur_y+dc[i]
#     if 0<=nx<n and 0<=ny<m and field[nx][ny]==1:
#       dfs(nx,ny)

for _ in range(t):
  m,n,k = map(int,input().split())
  field = [[0 for col in range(m)] for row in range(n)]
  
  for i in range(k):
    x, y = map(int,input().split())
    field[y][x]=1

  ans=0
  for i in range(n):
    for j in range(m):
      if field[i][j]==1:
        # dfs 풀이
        #dfs(i,j)
        # bfs 풀이
        bfs(i,j)
        ans+=1
        
  print(ans)