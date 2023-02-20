import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {}
for i in range(1, n+1):
  graph[i] = []

low = 1
high = 1
for i in range(m):
  a, b, c = map(int ,input().split())
  high = max(high, c)
  graph[a].append((b, c))
  graph[b].append((a, c))

s, e = map(int, input().split())

def bfs(mid) :
  q = deque()
  q.append(s)
  visited = [0 for _ in range(n+1)]
  visited[s] = 1
  while q:
    cur_v = q.popleft()
    if cur_v == e:
      return True
    for v, length in graph[cur_v]:
      if not visited[v] and mid <= length:
        q.append(v)
        visited[v] = 1
  return False


while low <= high:
  mid = (low + high)//2
  
  if bfs(mid):
    low = mid + 1
  else:
    high = mid - 1

print(low-1)