import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
  for j in range(n):
    if space[i][j]==9:
      c_x, c_y = i, j 
      break  

dr = [-1, 0, 1, 0]
dc = [0, 1 ,0, -1]

def bfs(cur_x, cur_y, size):
  q = deque([(cur_x,cur_y)])
  visited = [[False for _ in range(n)] for _ in range(n)]
  visited[cur_x][cur_y] = True
  space[cur_x][cur_y] = 0
  candidate = []
  time = 0
  while q:
    if len(candidate)>0:
      return candidate, time
    time += 1
    for _ in range(len(q)):
      x, y = q.popleft()
      for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and space[nx][ny]<=size:
          if space[nx][ny]>0 and space[nx][ny]<size:
            candidate.append((nx,ny))
          visited[nx][ny]=True
          q.append((nx,ny))
  return candidate, time

ans = 0
feed = 0
size = 2
while True:
  cand, t = bfs(c_x,c_y,size)
  if len(cand)==0:
    print(ans)
    break
  c_x, c_y = sorted(cand,key = lambda x : (x[0], x[1]))[0]
  ans += t
  feed += 1
  if size == feed:
    size += 1
    feed = 0