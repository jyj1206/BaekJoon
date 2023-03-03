import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

flag = True
checked = [[False] * c for _ in range(r)]
def bfs(start_x, start_y):
  global flag
  q = deque([(start_x, start_y)])
  checked[start_x][start_y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and not checked[nx][ny]:
        if graph[nx][ny] == 'S':
          if graph[x][y] != 'W':
            graph[x][y] = 'D'
          else:
            flag = False
          continue
        checked[nx][ny] = True
        q.append((nx, ny))
  
for i in range(r):
  for j in range(c):
    if graph[i][j] == 'W' and not checked[i][j]:
      bfs(i, j)

if not flag:
  print(0)
else:
  print(1)
  for row in graph:
    print(''.join(row))
