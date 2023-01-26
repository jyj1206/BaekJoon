import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())

time=[-1]*100001
visited=[0]*100001

def bfs():
  queue= deque([n])
  time[n]=0
  visited[n]=1
  while queue:
    cur_v =queue.popleft()
    if cur_v==k:
      print(time[k])
      print(visited[k])
      return
    for v in (cur_v-1,cur_v+1,2*cur_v):
      if 0<=v<=100000:
        if time[v]==-1:
          time[v]=time[cur_v]+1
          visited[v]=visited[cur_v] 
          queue.append(v)
        elif time[v]==time[cur_v]+1:
          visited[v]+=visited[cur_v]

bfs()

# 내풀이
# def bfs():
#   queue= deque([n])
#   cnt=0
#   time[n]=0
#   level=-1
#   while queue:
#     cur_v =queue.popleft()
#     if cur_v==k:
#       cnt+=1
#       level=time[cur_v]
#       continue
#     else:
#       if level==time[cur_v]:
#         continue
#     for v in (cur_v-1,cur_v+1,2*cur_v):
#       if 0<=v<=100000:
#         if time[v]==-1:
#           time[v]=time[cur_v]+1
#           queue.append(v)
#         elif time[v]==time[cur_v]+1:
#           queue.append(v)
  
#   print(level)
#   print(cnt)
  
# bfs()