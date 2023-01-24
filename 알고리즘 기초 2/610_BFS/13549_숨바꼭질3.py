import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n,k = map(int,input().split())
INF=int(1e9)



# 다익스트라 풀이
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