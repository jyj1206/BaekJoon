import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, E = map(int,input().split())
INF = int(1e9)
graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))
  graph[v].append((u,w))

v1,v2=map(int,input().split())

def dijkstra(start):
  h=[]
  distance=[INF]*(n+1)
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
  return distance


original=dijkstra(1)
sTov1 = original[v1]
sTov2 = original[v2]

v1_distance=dijkstra(v1)
v1_v2 = v1_distance[v2]
v1Ton = v1_distance[n]

v2_distance=dijkstra(v2)
v2Ton = v2_distance[n]

# 1->v1->v2->n
case_1 = sTov1+v1_v2+v2Ton
# 1->v2->v1->n
case_2 = sTov2+v1_v2+v1Ton

result = min(case_1,case_2)
if result>=INF:
  print(-1)
else:
  print(result)

# original_distance = dijkstra(1)
# v1_distance = dijkstra(v1)
# v2_distance = dijkstra(v2)

# v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
# v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

# result = min(v1_path, v2_path)
# print(result if result < INF else -1)