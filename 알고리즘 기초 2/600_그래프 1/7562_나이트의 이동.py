import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

def bfs(s_x,s_y,f_x,f_y):
  queue=deque([(s_x,s_y)])
  chess[s_x][s_y]=1
  while queue:
    x,y=queue.popleft()
    if x==f_x and y==f_y:
      print(chess[f_x][f_y]-1)
      return
    for i in range(8):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<l and 0<=ny<l and chess[nx][ny]==0:
        chess[nx][ny]=chess[x][y]+1
        queue.append((nx,ny))
  
for i in range(t):
  l = int(input())
  s_x,s_y=map(int,input().split())
  f_x,f_y=map(int,input().split())
  chess=[[0 for col in range(l)] for row in range(l)]
  bfs(s_x,s_y,f_x,f_y)
  