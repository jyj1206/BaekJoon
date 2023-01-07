import sys
input = sys.stdin.readline
t = int(input())
n_max=1001
dp=[[0 for j in range(n_max)]for i in range(n_max)]

dp[1][1]=1
dp[2][1]=1
dp[2][2]=1
dp[3][1]=1
dp[3][2]=2
dp[3][3]=1

for i in range(4,n_max):
  for j in range(1,i+1):
      dp[i][j]=(dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1])%1000000009

for i in range(t):
  x,y = map(int,input().split())
  print(dp[x][y])