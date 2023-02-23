import sys
from itertools import combinations
input = sys.stdin.readline
n, l, r, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

cnt = 0
for i in range(2, n + 1):
  for combi in combinations(a, i):
    if l <= sum(combi) <= r and combi[-1] - combi[0] >= x:
      cnt += 1

print(cnt)