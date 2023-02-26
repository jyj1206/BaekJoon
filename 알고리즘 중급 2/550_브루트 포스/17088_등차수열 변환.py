import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
b = list(map(int, input().split()))

oper = [-1, 0, 1]

def bfs(case):
  global result
  q = deque(case)
  while q:
    first, idx, deviation, cnt= q.popleft()
    if idx == n - 1:
      result = min(result, cnt)
      continue
    for i in oper:
      second = b[idx + 1] + i
      d = second - first
      if deviation != d:
        continue
      cnt += abs(i)
      q.append((second, idx + 1, deviation ,cnt))

if n == 1:
  print(0)
else:
  INF = int(1e9)
  result = INF
  d_case = []
  for i in oper:
    for j in oper:
      first = b[0] + i
      second = b[1] + j
      deviation = second - first
      cnt = abs(i) + abs(j)
      d_case.append((second, 1, deviation, cnt))
  
  bfs(d_case)
  
  if result != INF:
    print(result) 
  else:
    print(-1)