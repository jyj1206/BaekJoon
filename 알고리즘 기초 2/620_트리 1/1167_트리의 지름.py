import sys
input = sys.stdin.readline

n=int(input())
graph={}

for i in range(1,n+1):
  graph[i]=[]
  
for i in range(n):
  row=list(map(int,input().split()))
  i=1
  while row[i]!=-1:
    graph[row[0]].append((row[i],row[i+1]))
    i+=2
    
max_sum=0
max_sum_idx=-1

def dfs(cur_v,sum):
  global max_sum_idx, max_sum
  if max_sum<sum:
    max_sum=sum
    max_sum_idx=cur_v
  visited[cur_v]=1
  for (next_v,cost) in graph[cur_v]:
    if not visited[next_v]:
      dfs(next_v,sum+cost)

visited=[0]*(n+1)
dfs(1,0)

visited=[0]*(n+1)
dfs(max_sum_idx,0)

print(max_sum)