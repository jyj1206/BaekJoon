import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
lec = []
max_d  = 0
for _ in range(n):
  p, d = map(int, input().split())
  lec.append((d, p))
  max_d = max(max_d, d)

lec.sort(reverse=True)

i = 0
h = []
ans = 0
for day in range(max_d, 0, -1):
  while i<n and day <= lec[i][0]:
    heappush(h, -lec[i][1])
    i+=1
  
  if h:
    p = heappop(h)
    ans += -p
print(ans)