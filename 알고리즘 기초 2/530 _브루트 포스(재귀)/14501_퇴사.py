import sys
input = sys.stdin.readline
n = int(input())
t=[]
p=[]
for i in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)

dp=[0]*(n+1)

for i in range(n-1,-1,-1):
  if t[i]+i>n:
    dp[i]=dp[i+1]
  else:
    dp[i]=(dp[i+t[i]]+p[i],dp[i+1])

print(dp)
# 브루트 포스
# ans=0
# def dfs(day,sum):
#   global ans
#   if day>n:
#     return
#   if day==n:
#     ans=max(ans,sum)
#     return
  
#   dfs(day+1,sum)
#   dfs(day+t[day],sum+p[day])

# dfs(0,0)
# print(ans)