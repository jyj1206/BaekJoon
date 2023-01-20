import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph={}

for i in range(1,n+1):
  graph[i]=[]

for i in range(n-1):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  
order=list(map(int,input().split()))

dfs_order=[0]*(n+1)

for i in range(n):
  dfs_order[order[i]]=i

for i in range(1,n+1):
  graph[i].sort(key = lambda x : dfs_order[x])

visited=[0]*(n+1)

result=[]
def dfs(cur_v):
  visited[cur_v]=1
  result.append(cur_v)
  for v in graph[cur_v]:
    if not visited[v]:
      dfs(v)

# idx=0
# def dfs(cur_v):
#   global idx
#   visited[cur_v]=1
#   if order[idx]==cur_v:
#     idx+=1
#   else :
#     return 0
  
#   for v in graph[cur_v]:
#     if not visited[v]:
#       flag=dfs(v)
#       if not flag:
#         return 0
#   return 1
# ans=dfs(1)
# print(ans)
dfs(1)

print(1 if result == order else 0)