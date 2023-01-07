# 풀이 1 
# n, k = map(int,input().split())
# dp=[[0 for j in range(k+1)]for i in range(n+1)]

# for i in range(n+1):
#   dp[i][1]=1
# for i in range(k+1):
#   dp[0][i]=1

# mod=1000000000

# for i in range(1,n+1):
#   for j in range(2,k+1):
#     for c in range(i+1):
#       dp[i][j]+=dp[c][j-1]%mod

# print(dp[n][k]%mod)

#풀이 2
n,k = map(int,input().split())
dp=[1 for i in range(n+1)]
mod=1000000000
for i in range(2,k+1):
  for j in range(1,n+1):
    dp[j]+=dp[j-1]%mod

print(dp[-1]%mod)