from collections import deque
import sys
input = sys.stdin.readline
_deque =deque()

n = int(input())
for i in range(n):
  order = input().split()
  if order[0]=='push_front':
    _deque.appendleft(int(order[1]))
  elif order[0]=='push_back':
    _deque.append(int(order[1]))
  elif order[0]=='pop_front':
    if not _deque:
      print(-1)
    else:
      print(_deque.popleft())
  elif order[0]=='pop_back':
    if not _deque:
      print(-1)
    else:
      print(_deque.pop())
  elif order[0]=='empty':
    if not _deque:
      print(1)
    else:
      print(0)
  elif order[0]=='size':
    print(len(_deque))
  elif order[0]=='front':
    if not _deque:
      print(-1)
    else:
      print(_deque[0])
  else:
    if not _deque:
      print(-1)
    else:
      print(_deque[-1])