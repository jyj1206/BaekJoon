import sys
from collections import deque
input = sys.stdin.readline
buffer=int(input())
queue=deque()
while(True):
  n = int(input())
  if n==-1:
    if queue:
      print(' '.join(map(str,queue)))
    else:
      print('empty')
    break
  elif n==0:
    queue.popleft()
  else:
    if len(queue)!=buffer:
      queue.append(n)
