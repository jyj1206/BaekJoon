import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
ice = [i for i in range(1, n + 1)]
check = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  check[a][b] = True
  check[b][a] = True

cnt = 0
for a, b, c in combinations(ice, 3):
  if check[a][b] or check[b][c] or check[a][c]:
    continue
  cnt += 1

print(cnt)