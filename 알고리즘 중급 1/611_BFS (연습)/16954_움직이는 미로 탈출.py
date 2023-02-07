import sys
from collections import deque
input = sys.stdin.readline
board = [list(input().strip()) for _ in range(8)]

walls = deque()
for i in range(8):
  for j in range(8):
    if board[i][j]=='#':
      walls.append((i,j))


move = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(0,0)]


def bfs(board):
  q=deque([(7,0)])
  while q:
    if len(walls)==0:
      print(1)
      return
    
    visited=set()
    for _ in range(len(q)):
      x, y = q.popleft()
      if board[x][y]=='#':
        continue
      for dr,dc in move:
        nx = x + dr
        ny = y + dc
        if 0<=nx<8 and 0<=ny<8 and board[nx][ny]=='.' and (nx,ny) not in visited:
          visited.add((nx,ny))
          q.append((nx,ny))

    next_board=[['.' for _ in range(8)] for _ in range(8)]
    for _ in range(len(walls)):
      x, y = walls.popleft()
      nx = x+1
      if nx==8:
        continue
      next_board[nx][y]='#'
      walls.append((nx,y))
    
    board=[row[:] for row in next_board]
    
  print(0)
  
bfs(board)