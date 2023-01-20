import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())

dist = [0]*1000001
def bfs(start_n):
  queue=deque([(start_n)])
  while queue:
    cur_n = queue.popleft()
    if cur_n==k:
      print(dist[cur_n])
      return
    for n in (cur_n-1,cur_n+1,cur_n*2):
      if 0<=n<=100000 and not dist[n]:
        dist[n]=dist[cur_n]+1
        queue.append(n)
        
bfs(n)