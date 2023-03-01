import sys
input = sys.stdin.readline

def move(x, y, i):
  move_cnt = 0
  nx = x
  ny = y
  while True:
    nx += dx[i]
    ny += dy[i]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
      graph[nx][ny] = '*'
      move_cnt += 1
    else:
      nx -= dx[i]
      ny -= dy[i]
      break
  return nx, ny, move_cnt

def back_move(nx, ny, i, move_cnt):
  for j in range(move_cnt):
    graph[nx - (dx[i] * j)][ny - (dy[i] * j)] = '.'

def dfs(x, y, cnt, depth):
  global result
  if depth > result:
    return
  
  if cnt == 0:
    result = min(result, depth)
    return

  for i in range(4):
    nx, ny, move_cnt = move(x, y, i)
    if move_cnt == 0:
      continue
    dfs(nx, ny, cnt - move_cnt, depth + 1)
    back_move(nx, ny, i, move_cnt)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    
t = 1
while True:
  try :
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    cnt  = sum([row.count('.') for row in graph])
    INF = int(1e9)
    result = INF
    for i in range(n):
      for j in range(m):
        if graph[i][j] == '.':
          graph[i][j] = '*'
          dfs(i, j, cnt - 1, 0)
          graph[i][j] = '.'
    print(f'Case {t}:' , -1 if result == INF else result)
    t += 1
  except :
    break
