import sys
input = sys.stdin.readline
n = int(input())
w=[list(map(int,input().split()))for _ in range(n)]
ans=int(2e9)
visited=[0]*n

def dfs(start,prev,cost):
  global ans
  if cost>ans:
    return
  
  if sum(visited)==n:
    if w[prev][start]!=0:
      ans=min(ans,cost+w[prev][start])
    return
  
  for i in range(n):
    if w[prev][i]!=0 and visited[i]==0:
      visited[i]=1
      dfs(start,i,cost+w[prev][i],visited)
      visited[i]=0

for i in range(n):
  visited[i]=1
  dfs(i,i,0)
  visited[i]=0

print(ans)



# visited=[]
# def dfs(start,prev,cost,visited):
#   global ans
#   if cost>ans:
#     return
  
#   if len(visited)==n:
#     if w[prev][start]!=0:
#       ans=min(ans,cost+w[prev][start])
#     return
  
#   for j in range(n):
#     if w[prev][j]!=0 and j not in visited:
#       visited.append(j)
#       dfs(start,j,cost+w[prev][j],visited)
#       visited.pop()

# for i in range(n):
#   dfs(i,i,0,[i])

# print(ans)