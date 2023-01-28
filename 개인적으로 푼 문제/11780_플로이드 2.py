import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph=[[INF for j in range(n+1)] for i in range(n+1)]

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a][b]=min(graph[a][b],c)

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0  

p=[[-1 for j in range(n+1)] for i in range(n+1)]

def fw():
  for k in range(1,n+1):
    for i in range(1,n+1):
      for j in range(1,n+1):
        if graph[i][k]+graph[k][j]<graph[i][j]:
          graph[i][j]=graph[i][k]+graph[k][j]
          p[i][j]=k

def inorder(i,j):
  if p[i][j]!=-1:
    inorder(i,p[i][j])
    result.append(p[i][j])
    inorder(p[i][j],j)

fw()

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==INF:
      print(0,end=" ")
    else:
      print(graph[i][j],end=" ")
  print()

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==0 or graph[i][j]==INF:
      print(0)
    else:
      result=[]
      result.append(i)
      inorder(i,j)
      result.append(j)
      print(len(result),*result)