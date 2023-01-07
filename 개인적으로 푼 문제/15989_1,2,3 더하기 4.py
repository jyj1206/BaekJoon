import sys
input = sys.stdin.readline
t=int(input())
# 1로 끝나는 경우
dp=[1]*10001
# 2로 끝나는 경우
for i in range(2,10001):
  dp[i]+=dp[i-2]
# 3로 끝나는 ㄱ경우
for i in range(3,10001):
  dp[i]+=dp[i-3]

for i in range(t):
  n=int(input())
  print(dp[n])

# 내 풀이
# import sys
# input = sys.stdin.readline
# t = int(input())
# dp=[[0,0,0] for i in range(10001)]
# dp[1]=[1,0,0]
# dp[2]=[1,1,0]
# dp[3]=[1,1,1]

# for i in range(4,10001):
#   dp[i][0]=dp[i-1][0]
#   dp[i][1]=dp[i-2][1]+dp[i-2][0]
#   dp[i][2]=dp[i-3][2]+dp[i-3][1]+dp[i-3][0]

# for i in range(t):
#   n=int(input())
#   print(sum(dp[n]))