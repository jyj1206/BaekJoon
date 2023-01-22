import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n=int(input())
tree={}
for i in range(1,n+1):
  tree[i]=[]
  
for i in range(n-1):
  p,c = map(int,input().split())
  tree[p].append(c)
  tree[c].append(p)

ans=[0]*(n+1) 
def dfs(cur_v):
  for v in tree[cur_v]:
    if ans[v]==0:
      ans[v]=cur_v
      dfs(v)

dfs(1)

for i in range(2,n+1):
  print(ans[i])
