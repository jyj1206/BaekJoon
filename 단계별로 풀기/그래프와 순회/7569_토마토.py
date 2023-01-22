import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int,input().split())

boxs=[]
tomato=0
day=0

for i in range(h):
  box=[]
  for j in range(n):
    row = list(map(int,input().split()))
    tomato+=row.count(0)
    box.append(row)
  boxs.append(box)

d=[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def bfs(start_tomato):
  global day
  cnt=0
  queue=deque(start_tomato)
  while queue:
    x,y,z=queue.popleft()
    for i in range(6):
      nx=x+d[i][0]
      ny=y+d[i][1]
      nz=z+d[i][2]
      if 0<=nx<h and 0<=ny<n and 0<=nz<m and not boxs[nx][ny][nz]:
        boxs[nx][ny][nz]=boxs[x][y][z]+1
        queue.append((nx,ny,nz))
        cnt+=1
        day=max(day,boxs[nx][ny][nz]-1)
  return cnt

if tomato==0:
  print(day)
else:
  tomato_index=[]
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if boxs[i][j][k]==1:
          tomato_index.append((i,j,k))
  ans=bfs(tomato_index)
  ans-=tomato
  print(day if ans==0 else -1)