import sys
input = sys.stdin.readline
n=int(input())
a=sorted([list(map(int,input().split())) for i in range(n)])

dp=[1]*n
for i in range(n):
  for j in range(i):
    if a[j][1]<a[i][1]:
      dp[i]=max(dp[j]+1,dp[i])

print(n-max(dp))
