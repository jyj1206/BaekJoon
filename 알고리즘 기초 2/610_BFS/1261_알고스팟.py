import sys
from collections import deque
input = sys.stdin.readline
# m : 가로, n : 세로
m,n = map(int,input().split())
maze = [list(map(int,input().strip())) for i in range(n)]

dr=[-1,0,1,0]
dc=[0,1,0,-1]
visited=[[-1 for j in range(m)] for i in range(n)]

def _0_1_bfs():
  deq=deque([(0,0)])
  visited[0][0]=0
  while deq:
    x,y=deq.popleft()
    if visited[n-1][m-1]!=-1:
      print(visited[n-1][m-1])
      return
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
        if maze[nx][ny]:
          deq.append((nx,ny))
          visited[nx][ny]=visited[x][y]+1
        else:
          deq.appendleft((nx,ny))
          visited[nx][ny]=visited[x][y]

_0_1_bfs()