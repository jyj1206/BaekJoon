import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


visited = [False * [m] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

def bfs(s_x, s_y):
  q = deque([(s_x, s_y)])
  each_cnt = 1
  edge = set()
  visited[s_x][s_y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if board[nx][ny] == 2:
          each_cnt += 1
          q.append((nx, ny))
        elif board[nx][ny] == 0:
          edge.add((x, y))
        visited[nx][ny] = True
  return each_cnt, edge

def valid(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
      return False
  return True
cnt = 0
group = []
edge_check = []
blank = []
for i in range(n):
  for j in range(m):
    if not visited[i][j] and board[i][j] == 2:
      each_cnt, edge = bfs(i, j)
      cnt += each_cnt
      group.append(each_cnt)
      edge_check.append(edge)
    elif board[i][j] == 0:
      blank.append((i,j))

result = 0
for ((x1, y1), (x2, y2)) in combinations(blank, 2):
  board[x1][y1] = 1
  board[x2][y2] = 1
  reserve_cnt = cnt
  case = 0
  for i in range(len(edge_check)):
    if case + reserve_cnt < result:
      break
    flag = True
    for (x, y) in edge_check[i]:
      if not valid(x,y):
        flag = False
        break
    if flag :
      reserve_cnt -= group[i]
      case += group[i]
  
    
  

  board[x1][y1] = 0
  board[x2][y2] = 0