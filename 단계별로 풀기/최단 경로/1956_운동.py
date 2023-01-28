import sys
input= sys.stdin.readline
from heapq import heappop, heappush
v, e = map(int,input().split())
INF = int(1e9)

graph={}
for i in range(1,v+1):
  graph[i]=[]

h=[]
distance=[[INF for j in range(v+1)] for i in range(v+1)]
for i in range(e):
  a,b,c= map(int,input().split())
  graph[a].append((b,c))
  distance[a][b]=c
  heappush(h,(c,b,a))

def dijkstra():
  while h:
    dist,cur_v,start=heappop(h)
    if start==cur_v:
      return dist
    if distance[start][cur_v]<dist:
      continue
    for next_v, weight in graph[cur_v]:
      cost=dist+weight
      if cost<distance[start][next_v]:
        distance[start][next_v]=cost
        heappush(h,((cost,next_v,start)))
  return -1

print(dijkstra())


# 플로이드 워셜 풀이 -> python 시간초과
# import sys
# v, e = map(int,input().split())
# INF = int(1e9)
# graph = [[INF for j in range(v+1)] for i in range(v+1)]

# for i in range(e):
#   a,b,c = map(int,input().split())
#   graph[a][b]=c
  
# for k in range(1,v+1):
#   for i in range(1,v+1):
#     for j in range(1,v+1):
#       graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
      
# ans=INF
# for i in range(1,v+1):
#   ans=min(ans,graph[i][i])

# print(ans if ans!=INF else -1)