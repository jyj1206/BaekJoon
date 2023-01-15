t=int(input())
#브루트 포스
def dfs(n,sum):
  global cnt
  if sum>n:
    return
  if sum==n:
    cnt+=1
    return
  for i in (1,2,3):
    sum+=i
    dfs(n,sum)
    sum-=i
    
    
for i in range(t):
  cnt=0
  dfs(int(input()),0)
  print(cnt)


# 동적계획법
# case = [int(input()) for _ in range(t)]
# n=max(case)
# dp=[0,1,2,4]+[0]*(n-3)

# for i in range(4,n+1):
#   dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

# for i in case:
#   print(dp[i])