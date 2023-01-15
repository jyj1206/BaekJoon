import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
state = []
for i in range(n):
  state.append(list(map(int,input().split())))
  
h = list(range(n))
min_diff=int(2e9)

for i in range(1,n//2+1):
  for start_list in combinations(h,i):
    link_list=set(h)-set(start_list)
    start=0
    link=0
    for x in start_list:
      for y in start_list:
        start+=state[x][y]
    
    for x in link_list:
      for y in link_list:
        link+=state[x][y]
        
    min_diff=min(min_diff,abs(start-link))

print(min_diff)  





# 시간 초과
# visited=[0]*n
# def dfs(depth):
#   global min_diff
  
#   if depth==n:
#     team_a=0
#     team_b=0
#     for i in range(n):
#       for j in range(n):
#         if visited[i]==1 and visited[j]==1:
#           team_a+=state[i][j]
#         if visited[i]==0 and visited[j]==0:
#           team_b+=state[i][j]
#     min_diff=min(abs(team_a-team_b),min_diff)
#     return
  
#   visited[depth]=1
#   dfs(depth+1)
#   visited[depth]=0
#   dfs(depth+1)

# dfs(0)

# print(min_diff)
