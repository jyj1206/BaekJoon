import sys
input = sys.stdin.readline
n,m = map(int,input().split())
INF=int(1e9)
edge=[]
dist=[INF]*(n+1)

graph={}
for i in range(1,n+1):
  graph[i]=[]

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  
def bf():
  dist[1]=0
  # n 라운드 실행 : n-1은 시작정점에서 부터 각 정점까지 가는데 지나 갈 수 있는 정점의 최대갯수,  1은 음의 간선 사이클 유무 확인 
  for i in range(n):
    # m 개의 간선에 대해서 동작
    for start in range(1,n+1):
      for end, cost in graph[start]:
        if dist[start]!=INF and dist[start]+cost<dist[end]:
          dist[end]=dist[start]+cost
          # n-1라운드에서도 최단거리 갱신이 생기는 경우
          if i == n-1:
            return True
  return False

negative_cycle=bf()

if negative_cycle:
  print(-1)
else:
  for i in range(2,n+1):
    print(-1 if dist[i]==INF else dist[i])