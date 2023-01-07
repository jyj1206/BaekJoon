n = int(input())
dp=[0 for i in range(n+1)]

for i in range(n+1):
  dp[i]=i
  for j in range(1,i):
    if j*j>i:
      break 
    if dp[i]>dp[i-j*j]+1:
      dp[i]=dp[i-j*j]+1
print(dp[n])