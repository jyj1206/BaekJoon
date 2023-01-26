# 0-1 bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
time=[-1]*100001

def _01_bfs():
  deq=deque([n])
  time[n]=0
  while deq:
    cur_v=deq.popleft()
    if cur_v==k:
      print(time[cur_v])
      return
    for v in cur_v-1, cur_v+1, cur_v*2:
      if 0<=v<=100000 and time[v]==-1:
        # 0인 경우
        if v==cur_v*2:
          deq.appendleft(v)
          time[v]=time[cur_v]
        # 1인 경우
        else:
          deq.append(v)
          time[v]=time[cur_v]+1

_01_bfs()

# 다익스트라 풀이
# import sys
# from heapq import heappop, heappush
# input = sys.stdin.readline
# n,k = map(int,input().split())
# INF=int(1e9)
# def dijkstra(start,end):
#   distance=[INF]*100001
#   h=[]
#   heappush(h,(0,start))
#   distance[start]=0
#   while h:
#     dist, cur = heappop(h)
#     if cur==end:
#       print(distance[end])
#       return
#     if distance[cur]<dist:
#       continue
#     for next in (cur-1,cur+1,2*cur):
#       if 0<=next<=100000:
#         if next==2*cur:
#           cost=dist
#         else:
#           cost=dist+1
#         if cost<distance[next]:
#           distance[next]=cost
#           heappush(h,(cost,next))

# dijkstra(n,k)