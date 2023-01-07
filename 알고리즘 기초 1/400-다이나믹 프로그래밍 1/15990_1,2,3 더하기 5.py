import sys
input=sys.stdin.readline
t=int(input())

dp=[[0,0,0] for i in range(100001)]
dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1]
for j in range(4,100001):
    dp[j][0]=(dp[j-1][1]+dp[j-1][2])%1000000009
    dp[j][1]=(dp[j-2][0]+dp[j-2][2])%1000000009
    dp[j][2]=(dp[j-3][0]+dp[j-3][1])%1000000009

for i in range(t):
  n=int(input())
  print(sum(dp[n])%1000000009)