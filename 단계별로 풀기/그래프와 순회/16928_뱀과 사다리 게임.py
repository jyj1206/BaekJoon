import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
dice=[1,2,3,4,5,6]
time=[0]*101
board=[i for i in range(101)]
for i in range(n+m):
  a,b = map(int,input().split())
  board[a]=b

def bfs():
  queue=deque([1])
  while queue:
    cur=queue.popleft()
    if cur==100:
      print(time[cur])
      return
    for d in dice:
      next=cur+d
      if next<=100 and not time[next]:
        time[next]=time[cur]+1
        if next==board[next]:
          queue.append(next)
        else:
          if not time[board[next]]:
            time[board[next]]=time[next]
            queue.append(board[next])
            
bfs()