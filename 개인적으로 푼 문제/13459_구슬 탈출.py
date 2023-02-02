import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

board= [list(input().strip()) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if board[i][j]=='R':
      r_x,r_y=i,j
    elif board[i][j]=='B':
      b_x,b_y=i,j
    elif board[i][j]=='O':
      end=i,j
      
dr=[-1,0,1,0]
dc=[0,1,0,-1]

visited=set()
def bfs(r_x, r_y, b_x,b_y, end):
  q = deque([(r_x,r_y,b_x,b_y,0)])
  visited.add((r_x,r_y,b_x,b_y))
  while q:
    crx, cry, cbx, cby, cost  = q.popleft()
    
    if cost==10:
      return 0
    
    for i in range(4):
      nrx, nry = crx, cry
      nbx, nby = cbx, cby
      
      # 해당 방향으로 기울였을때 둘 다 벽에 부딪히는 경우 
      if board[nrx+dr[i]][nry+dc[i]]=='#' and board[nbx+dr[i]][nby+dc[i]]=='#':
        continue
      
      # 하나의 구슬이 벽에 닿을 때까지 움직여줌
      red_flag=False
      blue_flag=False
      
      while board[nrx+dr[i]][nry+dc[i]]!='#' and board[nbx+dr[i]][nby+dc[i]]!='#'and not red_flag and not blue_flag:
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
        # 파란 구슬을 벽에 닿을 때 까지 움직임, 만약 파란 구슬이 빠지면 continue 아니면 1 반환
        while board[nbx+dr[i]][nby+dc[i]]!='#' and not blue_flag:
          nbx=nbx+dr[i]
          nby=nby+dc[i]
          if (nbx,nby) == end:
            blue_flag=True
        
        if blue_flag:
          continue
        else:
          return 1
      # 둘다 안빠진 경우
      else:
        # 파란 구슬이 벽이나 다른 구슬에 안 닿은 경우 확인
        while board[nbx+dr[i]][nby+dc[i]]!='#' and (nbx+dr[i],nby+dc[i])!=(nrx,nry) and not blue_flag:
          nbx=nbx+dr[i]
          nby=nby+dc[i]
          if (nbx,nby) == end:
            blue_flag=True
        
        # 위의 코드가 돌아서 파란 구슬이 빠졌으면
        if blue_flag:
          continue
        
        # 빨간 구슬이 벽이나 다른 구슬에 안 닿은 경우 확인
        while board[nrx+dr[i]][nry+dc[i]]!='#' and (nrx+dr[i],nry+dc[i])!=(nbx,nby):
          nrx=nrx+dr[i]
          nry=nry+dc[i]
          if (nrx,nry) == end:
            return 1
          
        if (nrx,nry,nbx,nby) not in visited:
          q.append((nrx,nry,nbx,nby,cost+1))
          visited.add((nrx,nry,nbx,nby))
      
  return 0


print(bfs(r_x,r_y,b_x,b_y,end))