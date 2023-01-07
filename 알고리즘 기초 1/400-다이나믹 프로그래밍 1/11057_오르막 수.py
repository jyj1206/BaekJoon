n = int(input())
dp=[1]*10

for i in range(2,n+1):
  for j in range(10):
    for k in range(j+1,10):
      dp[j]+=dp[k]%10007
print(sum(dp)%10007)