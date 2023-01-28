import sys
from heapq import heappush,heappop
input = sys.stdin.readline
n = int(input())
m = int(input())
INF=int(1e9)


graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  x,y,w = map(int,input().split())
  graph[x].append((y,w))

a,b=map(int,input().split())

def dijkstra(start,end):
  h=[]
  distance=[INF]*(n+1)
  distance[start]=0
  heappush(h,(0,start))
  while h:
    dist, cur_v = heappop(h)
    if cur_v==end:
      print(dist)
      return
    if distance[cur_v]<dist:
      continue
    for i in graph[cur_v]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heappush(h,(cost,i[0]))
        
dijkstra(a,b)