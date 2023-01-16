import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int,input().split())

graph={}
for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  u, v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
  
visited=[False]*(n+1)

#dfs 풀이
def dfs(cur_v):
  visited[cur_v]=True
  for v in graph[cur_v]:
    if not visited[v]:
      dfs(v)

cnt=0
for i in range(1,n+1):
  if not visited[i]:
    cnt+=1
    dfs(i)

print(cnt)

# bfs 풀이
# def bfs(start_v):
#   visited[start_v]=True
#   queue=deque([start_v])
#   while queue:
#     cur_v=queue.popleft()
#     for v in graph[cur_v]:
#       if not visited[v]:
#         visited[v]=True
#         queue.append(v)
# cnt=0
# for i in range(1,n+1):
#   if not visited[i]:
#     cnt+=1
#     bfs(i)
# print(cnt)