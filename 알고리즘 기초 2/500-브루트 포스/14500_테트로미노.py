import sys
input = sys.stdin.readline

n, m = map(int,input().split())
paper=[list(map(int,input().split())) for i in range(n)]
visited=[[0 for j in range(m)] for i in range(n)]
max_value=max(map(max,paper))
ans=0

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(cur_x,cur_y,sum,cnt):
  global ans
  # 남은것으로는 아무리커도 현재 값보다 커지지 못하면 retrun
  if ans>sum+max_value*(4-cnt):
    return
  if cnt==4:
    ans=max(ans,sum)
    return
  for i in range(4):
    nx=cur_x+dr[i]
    ny=cur_y+dc[i]
    if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
      # 현재 두개의 노드만 추가된 상태의 현재 노드에서, 다음 노드를 추가시키만 다음 노드가 아닌 현재 노드에서 다시 dfs 실행함(예외 처리를 위해(ㅗ 모양))
      if cnt==2:
        visited[nx][ny]=1
        dfs(cur_x,cur_y,sum+paper[nx][ny],cnt+1)
        visited[nx][ny]=0
      visited[nx][ny]=1
      dfs(nx,ny,sum+paper[nx][ny],cnt+1)
      visited[nx][ny]=0

for i in range(n):
  for j in range(m):
    visited[i][j]=1
    dfs(i,j,paper[i][j],1)
    visited[i][j]=0

print(ans)

# # 풀이 2 - 예외 처리를 따로
# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# paper=[list(map(int,input().split())) for i in range(n)]
# visited=[[0 for j in range(m)] for i in range(n)]
# max_value=max(map(max,paper))
# ans=0

# dr = [-1,0,1,0]
# dc = [0,1,0,-1]

# def dfs(cur_x,cur_y,sum,cnt):
#   global ans
#   # 남은것으로는 아무리커도 현재 값보다 커지지 못하면 retrun
#   if ans>sum+max_value*(4-cnt):
#     return
#   if cnt==4:
#     ans=max(ans,sum)
#     return
#   for i in range(4):
#     nx=cur_x+dr[i]
#     ny=cur_y+dc[i]
#     if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
#       visited[nx][ny]=1
#       dfs(nx,ny,sum+paper[nx][ny],cnt+1)
#       visited[nx][ny]=0
##ㅗ 모양 예외처리
# def exce(x,y):
#   global ans
#   for i in range(4):
#     sum=paper[x][y]
#     for j in range(3):
#       idx=(i+j)%4
#       nx=x+dr[idx]
#       ny=y+dc[idx]
#       if 0<=nx<n and 0<=ny<m:
#         sum+=paper[nx][ny]
#       else:
#         sum=0
#         break
#     ans=max(sum,ans)
    

# for i in range(n):
#   for j in range(m):
#     visited[i][j]=1
#     dfs(i,j,paper[i][j],1)
#     visited[i][j]=0
#     exce(i,j)

# print(ans)
