import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(x,y):
  if 0<=x<n and 0<=y<n:
    return True
  return False

def merge(b,nx,ny,m,merged):
  fx = nx+dr[m]
  fy = ny+dc[m]
  # 앞선 좌표가 벽이 아니면서, 병합 된적이 없는 경우에 숫자가 같은경우
  if check(fx,fy) and not merged[fx][fy] and b[fx][fy]==b[nx][ny]:
    merged[fx][fy]=1
    b[fx][fy]*=2
    b[nx][ny]=0

def move(b,x,y,m,merged):
  if b[x][y]!=0:
    nx=x
    ny=y
    # 벽이나 다른 숫자에 도달하기 전까지 이동
    while check(nx+dr[m],ny+dc[m]) and b[nx+dr[m]][ny+dc[m]]==0:
      nx+=dr[m]
      ny+=dc[m]
    b[nx][ny], b[x][y] = b[x][y], b[nx][ny]
    # 병합
    merge(b,nx,ny,m,merged)

def direction(b,m):
  merged=[[0 for _ in range(n)] for _ in range(n)]
  # 상 0 하 1  좌 2 우 3
  if m==0:
    for x in range(n):
      for y in range(n):
        move(b,x,y,m,merged)
  elif m==1:
    for x in range(n-1,-1,-1):
      for y in range(n):
        move(b,x,y,m,merged)
  elif m==2:
    for y in range(n):
      for x in range(n):
        move(b,x,y,m,merged)
  else:
    for y in range(n-1,-1,-1):
      for x in range(n):
        move(b,x,y,m,merged)


def bfs(start):
  q = deque()
  cache=set()
  cache.add(tuple(map(tuple,start)))
  q.append((start,0))
  ans=max(map(max,start))
  while q:
    # 현재 보드, 이동한 횟수
    cur_board, cost= q.popleft()
    # 5번 이동한 경우
    if cost==5:
      return ans
    
    next_board = [row[:] for row in cur_board]
    for i in range(4):
      direction(next_board,i)
      
      # 이동 시킨 보드가 만들어진 적이 없는 경우
      c = tuple(map(tuple,next_board))
      if c not in cache:
        cache.add(c)
        q.append((next_board,cost+1))
        ans=max(ans,max(map(max,next_board)))
      next_board=[row[:] for row in cur_board]
  return ans

print(bfs(board))