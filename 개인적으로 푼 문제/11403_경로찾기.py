import sys
from collections import deque
input= sys.stdin.readline
n=int(input())
graph={}

for i in range(n):
  graph[i]=[]

for i in range(n):
  row=list(map(int,input().split()))
  for j in range(n):
    if row[j]:
      graph[i].append(j)

#bfs
visited=[[0 for j in range(n)] for i in range(n)]
def bfs(start):
  queue=deque([start])
  while queue:
    cur_v=queue.popleft()
    for v in graph[cur_v]:
      if not visited[start][v]:
        visited[start][v]=1
        queue.append(v)

for i in range(n):
  bfs(i)

for i in range(n):
  print(*visited[i])


# dfs
# def dfs(cur_v):
#   for v in graph[cur_v]:
#     if not visited[v]:
#       visited[v]=1
#       dfs(v)


# for i in range(n):
#   visited=[0 for j in range(n)]
#   dfs(i)
#   print(' '.join(map(str,visited)))
  

# 플로이드 와샬
# import sys
# input =sys.stdin.readline
# n= int(input())
# graph=[list(map(int,input().split())) for i in range(n)]

# for k in range(n):
#   for i in range(n):
#     for j in range(n):
#       if graph[i][k]+graph[k][j]==2:
#         graph[i][j]=1

# for i in range(n):
#   for j in range(n):
#       print(graph[i][j],end=" ")
#   print()