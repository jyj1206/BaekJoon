t = int(input())
n=1000000
dp=[0,1,2,2,3,3,6]+[0]*(n-6)
for i in range(7,n+1):
  dp[i]=(dp[i-2]+dp[i-4]+dp[i-6])%1000000009

for i in range(t):
  x=int(input())
  print(dp[x])