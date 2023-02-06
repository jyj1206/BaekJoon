import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(n)]
visited= [[0 for col in range(m)] for row in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs():
  # 현재x, 현재y, 벽 부순 개수
  q= deque([(0,0,0)])
  visited=[[[0 for col in range(m)] for row in range(n)] for dep in range(k+1)]
  visited[0][0][0]=1
  d_least=[[k+1 for col in range(m)] for row in range(n)]
  d_least[0][0]=0
  while q:
    x,y,d = q.popleft()
    if (x,y)==(n-1,m-1):
      print(visited[d][n-1][m-1])
      return
    for i in range(4):
      nx = x + dr[i]
      ny = y + dc[i]
      if 0<=nx<n and 0<=ny<m:
        if not board[nx][ny] and d < d_least[nx][ny] and not visited[d][nx][ny]:
          visited[d][nx][ny]=visited[d][x][y]+1
          q.append((nx,ny,d))
          d_least[nx][ny]=d
        
        elif board[nx][ny] and d<k and  d+1 < d_least[nx][ny] and not visited[d+1][nx][ny]:
          visited[d+1][nx][ny]=visited[d][x][y]+1
          q.append((nx,ny,d+1))
          d_least[nx][ny]=d+1
  print(-1)
  
bfs()