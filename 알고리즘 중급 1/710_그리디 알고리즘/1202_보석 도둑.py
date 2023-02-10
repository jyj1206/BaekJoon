import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())
jew = []
bag = []

for i in range(n):
  w, v = map(int, input().split())
  jew.append((w, v))

for i in range(k):
  c = int(input())
  bag.append(c)

bag.sort()
jew.sort()

ans = 0
h = []
j = 0
for i in range(k):
  # 가방보다 크기가 작거나 같은 보석들을 힙에 넣음
  while j < n and jew[j][0] <= bag[i]:
    heappush(h, (-jew[j][1], jew[j][0]))
    j += 1
    
  # 힙에 보석이 하나라도 있으면
  if h:
    v, w = heappop(h)
    ans += -v
    
print(ans)