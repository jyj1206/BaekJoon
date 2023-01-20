import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v=int(input())
e=int(input())
graph={}
visited=[0]*(v+1)
for i in range(1,v+1):
  graph[i]=[]
  
for i in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(cur_v):
  visited[cur_v]=1
  for v in graph[cur_v]:
    if not visited[v]:
      dfs(v)

dfs(1)
print(sum(visited)-1)