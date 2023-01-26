import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board=[]
g_r_board=[]
for i in range(n):
  row=input().strip()
  g_r_row=row.replace('R','G')
  board.append(list(row))
  g_r_board.append(list(g_r_row))
  
dr=[-1,0,1,0]
dc=[0,1,0,-1]
visited=[[0 for j in range(n)] for i in range(n)]
g_r_visited=[[0 for j in range(n)] for i in range(n)]

def dfs(cur_x,cur_y,graph,visit):
  visit[cur_x][cur_y]=1
  for i in range(4):
    nx=cur_x+dr[i]
    ny=cur_y+dc[i]
    if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
      if graph[nx][ny]==graph[cur_x][cur_y]:
        dfs(nx,ny,graph,visit)

ans=[0]*2
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i,j,board,visited)
      ans[0]+=1
    if not g_r_visited[i][j]:
      dfs(i,j,g_r_board,g_r_visited)
      ans[1]+=1

print(*ans)