import sys
from heapq import heappush, heappop
input = sys.stdin.readline
# 정점 개수, 간선 개수
V, E = map(int,input().split())
# 시작 정점
K = int(input())
INF = int(1e9)

graph={}
for i in range(1,V+1):
  graph[i]=[]

for i in range(E):
  u,v,w = map(int,input().split())
  # 정점, 가중치 순으로 저장
  graph[u].append((v,w))

distance=[INF]*(V+1)
def dijkstra(start):
  h=[]
  distance[start]=0
  heappush(h,(0,start))
  while h:
    dist, cur_v = heappop(h)
    if distance[cur_v]<dist:
      continue
    for i in graph[cur_v]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heappush(h,(cost,i[0]))
        
dijkstra(K)  

for i in range(1,V+1):
  if distance[i]==INF:
    print('INF')
  else:
    print(distance[i])