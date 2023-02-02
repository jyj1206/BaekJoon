import sys
from collections import deque
n, m = map(int,input().split())

board = [list(input()) for i in range(n)]

for i in range(n):
  for j in range(m):
    if board[i][j]=='R':
      r_x, r_y = i,j
    elif board[i][j]=='B':
      b_x, b_y = i,j
    elif board[i][j]=='O':
      end = (i,j)

dr=[-1,0,1,0]
dc=[0,1,0,-1]
visited=set()
def bfs():
  q = deque([(r_x,r_y,b_x,b_y,0)])
  visited.add((r_x,r_y,b_x,b_y))
  
  while q:
    crx,cry,cbx,cby, cost=q.popleft()
    # 10번 움직였으면
    if cost==10:
      return -1
    for i in range(4):  
      # 해당 이동이 처음 부터 둘 다 벽에 부딪히게 하는 경우
      if board[crx+dr[i]][cry+dc[i]]=='#' and board[cbx+dr[i]][cby+dc[i]]=='#':
        continue
      nrx, nry, nbx, nby = crx, cry, cbx, cby
      red_flag=False
      blue_flag=False
      # 먼저 하나의 구슬이 벽에 닿거나 구멍에 빠질 떄까지 반복
      while not red_flag and not blue_flag and board[nrx+dr[i]][nry+dc[i]]!='#' and board[nbx+dr[i]][nby+dc[i]]!='#':
        nrx=nrx+dr[i]
        nry=nry+dc[i]
        nbx=nbx+dr[i]
        nby=nby+dc[i]
        if (nrx,nry)==end:
          red_flag=True
        if (nbx,nby)==end:
          blue_flag=True
          
      # 파란 구슬이 빠진 경우
      if blue_flag:
        continue
      # 빨간 구슬이 빠진 경우
      elif red_flag:
        while not blue_flag and board[nbx+dr[i]][nby+dc[i]]!='#' :
          nbx=nbx+dr[i]
          nby=nby+dc[i]
          if (nbx,nby)==end:
            blue_flag=True
        if blue_flag:
          continue
        else:
          return cost+1
      # 둘다 안 빠진 경우
      else:
        # 파란 구슬이 벽이나 다른 구슬에 안닿은 경우
        while not blue_flag and board[nbx+dr[i]][nby+dc[i]]!='#' and (nbx+dr[i],nby+dc[i])!=(nrx,nry):
          nbx=nbx+dr[i]
          nby=nby+dc[i]
          if (nbx,nby)==end:
            blue_flag=True
        
        # 파란 구슬이 빠진 경우
        if blue_flag:
          continue
        
        # 빨간 구슬이 벽이나 다른 구슬에 안닿은 경우
        while board[nrx+dr[i]][nry+dc[i]]!='#' and (nrx+dr[i],nry+dc[i])!=(nbx,nby):
          nrx=nrx+dr[i]
          nry=nry+dc[i]
          if (nrx,nry)==end:
            return cost+1
        
        if (nrx,nry,nbx,nby) not in visited:
          visited.add((nrx,nry,nbx,nby))
          q.append((nrx,nry,nbx,nby,cost+1))
    
  return -1

print(bfs())