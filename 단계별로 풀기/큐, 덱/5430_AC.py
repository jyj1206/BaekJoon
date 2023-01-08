import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
  ps = input().rstrip()
  n = int(input())
  arr = input()
  if n==0:
    deq=deque()
  else:
    deq=deque(map(int,arr.rstrip().replace('[','').replace(']','').split(',')))
  s=0
  for p in ps:
    if p=='R':
      s+=1
    else:
      if deq:
        if s%2==0:
          deq.popleft()
        else:
          deq.pop()
      else:
        print('error')
        break
  else:
    if s%2!=0:
      deq.reverse()
    ans=','.join(map(str,deq))
    print(f'[{ans}]')