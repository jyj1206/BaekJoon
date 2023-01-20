import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board=[list(map(int,input().split())) for i in range(n)]
visited=[[0 for j in range(n)] for i in range(n)]
bridge=[[0 for j in range(n)] for i in range(n)]

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def found_boader(x,y,cnt):
  queue=deque([(x,y)])
  visited[x][y]=cnt
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
        if board[nx][ny]==1:
          visited[nx][ny]=cnt
          queue.append((nx,ny))
        else:
          border.add((x,y,cnt))

def bfs(border):
  queue=deque(border)
  while queue:
    x,y,island=queue.popleft()
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<n:
        if not visited[nx][ny]:
          bridge[nx][ny]=bridge[x][y]+1
          visited[nx][ny]=island
          queue.append((nx,ny,island))
        else:
          # 다리가 이미 있는데, 서로 다른 섬에서 지어졌으면 
          if bridge[nx][ny] and visited[nx][ny]!=visited[x][y]: 
            return bridge[nx][ny]+bridge[x][y]
        

border=set()
cnt=1
for x in range(n):
  for y in range(n):
    if board[x][y]==1 and not visited[x][y]:
      found_boader(x,y,cnt)
      cnt+=1

ans=bfs(border)
print(ans)

