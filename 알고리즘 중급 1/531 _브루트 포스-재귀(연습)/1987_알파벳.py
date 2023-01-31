import sys
input = sys.stdin.readline
r,c = map(int,input().split())

board = [list(input().strip()) for _ in range(r)]

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def dfs(cur_x,cur_y,alpa,cnt):
  global ans
  ans = max(ans,cnt)
  for i in range(4):
    nx=cur_x+dr[i]
    ny=cur_y+dc[i]
    if 0<=nx<r and 0<=ny<c:
      if board[nx][ny] not in alpa:
        alpa.add(board[nx][ny])
        dfs(nx,ny,alpa,cnt+1) 
        alpa.remove(board[nx][ny])

ans=0
alpa=set([board[0][0]])
dfs(0,0,alpa,1)
    
print(ans)