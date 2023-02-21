import sys
n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]

for _ in range(m):
  x, y = map(int ,input().split())
  basket[x-1], basket[y-1] = basket[y-1], basket[x-1]

print(*basket)