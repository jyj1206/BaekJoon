import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
blank = []
for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      blank.append((i, j))
    elif board[i][j] == 2:
      cnt += 1

for ((x1, y1), (x2, y2)) in combinations(blank, 2):
  board[x1][y1] = 1
  board[x2][y2] = 1
  visited = [[False] * m for _ in range(m)]
  for i in range(n):
    for j in range(m):
      if board[i][j] == '2' and not visited[i][j]:
        pass
  board[x1][y1] = 0
  board[x2][y2] = 0