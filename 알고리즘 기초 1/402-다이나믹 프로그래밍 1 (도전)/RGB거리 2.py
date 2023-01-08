import sys
input =sys.stdin.readline
n = int(input())
color=[]
dp=[[0 for i in range(3)] for i in range(n)]

inf = int(2e9)

for i in range(n):
  color.append(list(map(int,input().split())))

ans=inf
#red,green,blue 0, 1, 2
for fix_color in (0,1,2):
  dp[0]=[inf,inf,inf]
  
  dp[0][fix_color]=color[0][fix_color]
  
  for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color[i][2]
  
  for i in range(3):
    if i!=fix_color:
      ans=min(ans,dp[-1][i])

print(ans)
