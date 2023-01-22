import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

board=[list(map(int,input().strip())) for i in range(n)]

dr=[-1,0,1,0]
dc=[0,1,0,-1]

dist=[[[0]*2 for j in range(m)] for i in range(n)]

def bfs():
  queue=deque([(0,0,0)])
  dist[0][0][0]=1
  while queue:
    x,y,destroy=queue.popleft()
    if x==n-1 and y==m-1:
        print(dist[n-1][m-1][destroy])
        return
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<m:
        # 벽이 아닌경우 현재까지 파괴한적이 있냐 없냐에 관계없이
        if not board[nx][ny] and not dist[nx][ny][destroy]:
          dist[nx][ny][destroy]=dist[x][y][destroy]+1
          queue.append((nx,ny,destroy))
        # 벽인 경우면서 현재까지 파괴한적이 없으면
        elif board[nx][ny] and not destroy:
            dist[nx][ny][1]=dist[x][y][0]+1
            queue.append((nx,ny,1))
  print(-1)
  return

bfs()