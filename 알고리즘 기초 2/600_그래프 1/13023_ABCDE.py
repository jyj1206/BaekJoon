import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph={}
for i in range(n):
  graph[i]=[]
  
for i in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
  
flag=0

visited=[False]*n

def dfs(cur_v,depth):
  global flag
  visited[cur_v]=True
  if depth==4:
    flag=1
    return
  for v in graph[cur_v]:
    if not visited[v]:
      dfs(v,depth+1)
      visited[v]=False
      
for i in range(n):
  if flag==1:
    break
  dfs(i,0)
  visited[i]=False

print(flag)