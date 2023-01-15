import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n,m,r=map(int,input().split())

graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

visited=[0]*(n+1)

for i in range(1,n+1):
  graph[i].sort(reverse=True)

cnt=1

def dfs(cur_v):
  global cnt
  visited[cur_v]=cnt
  for v in graph[cur_v]:
    if visited[v]==0:
      cnt+=1
      dfs(v)
      
dfs(r)

for i in range(1,n+1):
  print(visited[i])