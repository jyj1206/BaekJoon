

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

# time[클립보드 갯수][현재 이모티콘 갯수]
time=[[-1 for j in range(1001)] for i in range(1001)]

def bfs():
  queue=deque([(0,1)])
  time[0][1]=0
  while queue:
    copy, cur=queue.popleft()
    if cur==n:
      print(time[copy][cur])
      return
    
    for next_copy, next_cur in ((cur,cur), (copy,copy+cur), (copy,cur-1)):
      if 0<=next_cur<=1000:
        if next_copy==0:
          continue
        
        if time[next_copy][next_cur]==-1:
          queue.append((next_copy,next_cur))
          time[next_copy][next_cur]=time[copy][cur]+1

bfs()