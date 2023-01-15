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

dfs_ans=[]

def dfs(cur_v):
  dfs_ans.append(cur_v)
  for v in graph[cur_v]:
    if v not in dfs_ans:
      dfs(v)

bfs_ans=[]

def bfs(start):
  queue=deque([start])
  bfs_ans.append(start)
  while queue:
    cur_v=queue.popleft()
    for v in graph[cur_v]:
      if v not in bfs_ans:
        queue.append(v)
        bfs_ans.append(v)

dfs(r)
bfs(r)

print(*dfs_ans)
print(*bfs_ans)