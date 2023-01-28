import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
dist=[[INF for j in range(n+1)] for i in range(n+1)]

for i in range(m):
  a,b,c = map(int,input().split())
  dist[a][b]=min(dist[a][b],c)
  
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      dist[i][j]=0

def fw():
  for k in range(1,n+1):
    for i in range(1,n+1):
      for j in range(1,n+1):
        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
  
fw()

for i in range(1,n+1):
  for j in range(1,n+1):
    if dist[i][j]==INF:
      print(0, end=' ')
    else:
      print(dist[i][j],end=' ')
  print()