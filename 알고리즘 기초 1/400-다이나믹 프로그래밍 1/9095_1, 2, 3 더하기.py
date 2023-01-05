t=int(input())
case = [int(input()) for _ in range(t)]
n=max(case)
dp=[0,1,2,4]+[0]*(n-3)

for i in range(4,n+1):
  dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in case:
  print(dp[i])