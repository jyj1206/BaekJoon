import sys
input = sys.stdin.readline
n, k = map(int, input().split())

weight = [0]
value = [0]

for i in range(n):
  w, v = map(int, input().split())
  weight.append(w)
  value.append(v)

dp = [[0 for j in range(k+1)] for i in range(n+1)]

for i in range(1, n+1):
  for w in range(1, k+1):
    if w - weight[i] >=0:
      dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
    else:
      dp[i][w] = dp[i-1][w]

print(dp[n][k])