import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline
n=int(input())
graph={}
for i in range(1,n+1):
  graph[i]=[]
  
for i in range(n):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  
# 방문X : 0, 방문o 순환선x : 1, 방문o 순환선o : -1
visited=[0]*(n+1)

# cycle에 속한 정점 찾기
def dfs(prev_v,cur_v):
  visited[cur_v]=1
  for v in graph[cur_v]:
    if not visited[v]:
      cycle_start_v=dfs(cur_v,v)
      # 사이클 시작 정점에 다시 도착할때까지 사이클에 속하는 정점의 visited 값을 -1로 변경
      if cycle_start_v!=-1 and cycle_start_v!=v:
        visited[v]=-1
        return cycle_start_v

    elif prev_v and prev_v!=v:
      visited[v]=-1
      return v
  # 사이클에 속한 정점이 아닌 경우 -1 반환
  return -1

def bfs():
  queue=deque()
  dist=[0]*(n+1)
  for i in range(1,n+1):
    if visited[i]==-1:
      queue.append(i)
      dist[i]=0
    else:
      dist[i]=-1
  while queue:
    cur_v=queue.popleft()
    for v in graph[cur_v]:
      if dist[v]==-1:
        queue.append(v)
        dist[v]=dist[cur_v]+1
  return dist

dfs(None,1)

dist=bfs()

for i in range(1,n+1):
  print(dist[i],end=' ')