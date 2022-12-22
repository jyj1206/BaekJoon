import sys
input = sys.stdin.readline
n = int(input())
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in (0,1,2):
        dp[i][j]+=min(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3])

print(dp)
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))