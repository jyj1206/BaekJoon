import sys
from collections import deque
input = sys.stdin.readline

n= int(input())
graph={}

for i in range(1,n+1):
  graph[i]=[]
  
for i in range(n-1):
  u, v, c = map(int,input().split())
  graph[u].append((v,c))
  graph[v].append((u,c))

def bfs(start_v):
  queue= deque([(start_v,0)])
  visited=[0]*(n+1)
  visited[start_v]=1
  max_cost=0
  max_cost_idx=start_v
  while queue:
    cur_v, cost = queue.popleft()
    for v, c in graph[cur_v]:
      if not visited[v]:
        visited[v]=1
        queue.append([v,(cost+c)])
        if max_cost<cost+c:
          max_cost=cost+c
          max_cost_idx=v
  return max_cost, max_cost_idx

_, y = bfs(1)

ans, _ = bfs(y)

print(ans)