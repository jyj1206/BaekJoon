from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,r = map(int,input().split())

graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1,n+1):
  graph[i].sort()

visited=[False]*(n+1)
dfs_ans=[]

def dfs(cur_v):
  dfs_ans.append(cur_v)
  visited[cur_v]=True
  for v in graph[cur_v]:
    if not visited[v]:
      dfs(v)

bfs_ans=[]

def bfs(start):
  queue=deque([start])
  visited[start]=True
  bfs_ans.append(start)
  while queue:
    cur_v=queue.popleft()
    for v in graph[cur_v]:
      if not visited[v]:
        visited[v]=True
        queue.append(v)
        bfs_ans.append(v)

dfs(r)
visited=[False]*(n+1)
bfs(r)

print(*dfs_ans)
print(*bfs_ans)