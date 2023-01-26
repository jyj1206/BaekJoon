import sys
from heapq import heappop, heappush
input = sys.stdin.readline
T= int(input())
INF=int(1e10)

def dijkstra(start):
  distance=[INF]*(n+1)
  h=[]
  distance[start]=0
  heappush(h,(0,start))
  while h:
    dist, cur_v = heappop(h)
    if distance[cur_v]<dist:
      continue
    for v, weight in graph[cur_v]:
      cost=dist+weight
      if cost<distance[v]:
        distance[v]=cost
        heappush(h,(cost,v))
  
  return distance

for _ in range(T):
  n, m, t = map(int,input().split())
  s, g, h = map(int,input().split())
  graph={}
  for i in range(1,n+1):
    graph[i]=[]

  for i in range(m):
    a,b,d= map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

  destination=[]
  for i in range(t):
    destination.append(int(input()))

  original_distance=dijkstra(s)
  g_distance=dijkstra(g)
  h_distance=dijkstra(h)

  # s->g->h
  case_1=original_distance[g]+g_distance[h]
  # s->h->g
  case_2=original_distance[h]+h_distance[g]

  ans=[]
  for d in destination:
    if original_distance[d]==min(case_1+h_distance[d],case_2+g_distance[d]):
      ans.append(d)

  print(*sorted(ans))