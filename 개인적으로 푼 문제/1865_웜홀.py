import sys
input = sys.stdin.readline

def bf():
  for i in range(n):
    for cur in range(1,n+1):
      for next, cost in graph[cur]:
        if dist[cur]+cost<dist[next]:
          dist[next]=dist[cur]+cost
          if i==n-1:
            print('YES')
            return
  print('NO')
  
tc = int(input())
for _ in range(tc):
  n,m,w = map(int,input().split())
  graph={}
  for i in range(1,n+1):
    graph[i]=[]
    
  for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

  for i in range(w):
    a,b,c = map(int,input().split())
    graph[a].append((b,-c))
    
  dist=[0]*(n+1)
  bf()