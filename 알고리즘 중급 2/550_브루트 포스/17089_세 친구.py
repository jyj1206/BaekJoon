import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {}

for i in range(1, n + 1):
  graph[i] = set()

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].add(b)
  graph[b].add(a)

INF = int(1e9)
result = INF
for a in range(1, n + 1):
  if len(graph[a]) < 2:
    continue
  for b in graph[a]:
    if len(graph[b]) < 2:
      continue
    for c in graph[b]:
      if c in graph[a]:
        result = min(result, len(graph[a]) + len(graph[b]) + len(graph[c]) - 6)
if result == INF:
  print(-1)
else:
  print(result)