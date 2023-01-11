n = int(input())
a = list(map(int,input().split()))
dp = [0]*n

dp[0]=a[0]
for i in range(1,n):
  dp[i]=a[i]
  for j in range(i):
    if a[i]>a[j]:
      dp[i]=max(dp[i],a[i]+dp[j])

print(max(dp))