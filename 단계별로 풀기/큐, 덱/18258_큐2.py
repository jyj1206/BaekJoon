from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue=deque()

for i in range(n):
  order=input().split()
  if order[0]=='push':
    queue.append(order[1])
  elif order[0]=='pop':
    print(queue.popleft() if queue else '-1')
  elif order[0]=='size':
    print(len(queue))
  elif order[0]=='empty':
    print('1' if not queue else '0')
  elif order[0]=='front':
    print(queue[0] if queue else '-1')
  else:
    print(queue[-1] if queue else '-1')