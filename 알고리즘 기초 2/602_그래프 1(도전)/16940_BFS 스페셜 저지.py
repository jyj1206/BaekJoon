import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph={}

for i in range(1,n+1):
  graph[i]=[]
  
for i in range(n-1):
  a,b= map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

order = list(map(int,input().split()))

bfs_order=[0]*(n+1)
for i in range(n):
  bfs_order[order[i]]=i

for i in range(1,n+1):
  graph[i].sort(key= lambda x: bfs_order[x])

print(graph)
visited=[0]*(n+1)

def bfs(start_v):
  i=0
  if order[0]==start_v:
    i+=1
    visited[start_v]=1
    queue=deque([start_v])
    while queue:
      cur_v=queue.popleft()
      for v in graph[cur_v]:
        if not visited[v]:
          if v==order[i]:
            queue.append(v)
            visited[v]=1
            i+=1
          else:
            return 0
    return 1
  else:
    return 0

# 내 풀이
# def bfs(start_v):
#   i=0
#   if order[0]==start_v:
#     i+=1
#   else:
#     return 0
#   visited[start_v]=1
#   queue=deque([start_v])
#   while queue:
#     cur_v=queue.popleft()
#     child_node=set()
#     for v in graph[cur_v]:
#       if not visited[v]:
#         visited[v]=1
#         child_node.add(v)
#     check_order=order[i:i+len(child_node)]
#     if set(child_node)!=set(check_order):
#       return 0
#     queue.extend(order[i:i+len(child_node)])
#     i+=len(child_node)
#   return 1

ans=bfs(1)

print(ans)