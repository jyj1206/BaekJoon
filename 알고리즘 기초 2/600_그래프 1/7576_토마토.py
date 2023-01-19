import sys
from collections import deque
input =sys.stdin.readline
m, n = map(int,input().split())

box = [list(map(int,input().split())) for row in range(n)]

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def bfs(box_t):
  queue=deque(box_t)
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<m and not box[nx][ny]:
        queue.append((nx,ny))
        box[nx][ny]=box[x][y]+1

def result():
  day=0
  for i in range(n):
    for j in range(m):
      if box[i][j]==0:
        print(-1)
        return
      elif box[i][j]!=-1:
        day=max(day,box[i][j])
  print(day-1)
  
tomato=[]
for i in range(n):
  for j in range(m):
    if box[i][j]==1:
      tomato.append((i,j))

bfs(tomato)

result()



