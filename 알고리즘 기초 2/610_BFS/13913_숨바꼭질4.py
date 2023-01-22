import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())

dist=[0]*100001
prev=[0]*100001

def bfs(start_v):
  queue=deque([start_v])
  while queue:
    cur_v=queue.popleft()
    if cur_v==k:
      print(dist[k])
      ans=deque([k])
      while ans[0]!=n:
        ans.appendleft(prev[ans[0]])
      print(*ans)
      return
    
    for v in (cur_v-1,cur_v+1,cur_v*2):
      if 0<=v<=100000 and not dist[v]:
        dist[v]=dist[cur_v]+1
        prev[v]=cur_v
        queue.append(v)

bfs(n)
