# dfs 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur_v,g):
  group[cur_v]=g
  for v in graph[cur_v]:
    if not group[v]:
      error=dfs(v,-g)
      if not error:
        return False
    elif group[cur_v]==group[v]:
      return False
  return True

t = int(input())
for _ in range(t):
  v, e =map(int,input().split())
  graph={}
  
  for i in range(1,v+1):
    graph[i]=[]
    
  for i in range(e):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

  group=[0]*(v+1)
  
  for i in range(1,v+1):
    if not group[i]:
      result = dfs(i,1)
      if not result:
        break
      
  print('YES' if result else 'NO')




# bfs 풀이
# from collections import deque
# import sys
# input = sys.stdin.readline
# def bfs(start_v):
#   queue=deque([start_v])
#   group[start_v]=1
#   while queue:
#     cur_v=queue.popleft()
#     for v in graph[cur_v]:
#       if not group[v]:
#         queue.append(v)
#         group[v]=group[cur_v]*-1
#       elif group[cur_v]==group[v]:
#         return False
#   return True

# t = int(input())

# for _ in range(t):
#   v, e =map(int,input().split())
#   graph={}
  
#   for i in range(1,v+1):
#     graph[i]=[]
    
#   for i in range(e):
#     x,y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)

#   group=[0]*(v+1)
  
#   for i in range(1,v+1):
#     if not group[i]:
#       result = bfs(i)
#       if not result:
#         break
      
#   print('YES' if result else 'NO')