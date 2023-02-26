import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      home.append((i, j))
    elif graph[i][j] == 2:
      chicken.append((i, j))

INF = int(1e9)
result = INF
for chicken_list in combinations(chicken, m):
  total = 0
  for h_x, h_y in home:
    chicken_distance = INF
    for c_x, c_y in chicken_list:
      chicken_distance = min(chicken_distance, abs(h_x - c_x) + abs(h_y - c_y))
    total += chicken_distance
  result = min(result, total)

print(result)