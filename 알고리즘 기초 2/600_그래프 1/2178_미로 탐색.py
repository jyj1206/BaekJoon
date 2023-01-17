import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
miro =[list(map(int,input().rstrip())) for _ in range(n)]
# 오른쪽, 아래, 왼쪽, 위
dr=[0,1,0,-1]
dc=[1,0,-1,0]
def bfs(x,y):
  queue=deque([(x,y)])
  while queue:
    x, y =queue.popleft()
    for i in range(4):
      nx=x+dr[i]
      ny=y+dc[i]
      if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1:
        miro[nx][ny]=miro[x][y]+1
        queue.append((nx,ny))

bfs(0,0)
print(miro[n-1][m-1])



# 내가 푼 풀이
# def bfs(x,y):
#   miro[x][y]=0
#   depth=1
#   queue=deque([(x,y,depth)])
#   while queue:
#     cur_x, cur_y,cur_depth = queue.popleft()
#     if cur_x==n-1 and cur_y==m-1:
#       print(cur_depth)
#       return
#     for i in range(4):
#       nx=cur_x+dr[i]
#       ny=cur_y+dc[i]
#       if 0<=nx<n and 0<=ny<m and miro[nx][ny]
#         miro[nx][ny]=0
#         queue.append((nx,ny,cur_depth+1))
#bfs(0,0)
