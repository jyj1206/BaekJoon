import sys
from collections import deque
input = sys.stdin.readline

n,m,r=map(int,input().split())

graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
  
visited=[0]*(n+1)
def bfs(start):
  cnt=1
  queue=deque([start])
  visited[start]=cnt
  while queue:
    cur_v=queue.popleft()
    for v in sorted(graph[cur_v],reverse=True):
      if visited[v]==0:
        cnt+=1
        queue.append(v)
        visited[v]=cnt
  
  for i in range(1,n+1):
    print(visited[i])
    
bfs(r)