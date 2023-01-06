import sys
input = sys.stdin.readline
t = int(input())
nums = [int(input()) for _ in range(t)]
max_num=max(nums)
dp=[0,1,2,4]+[0]*(max_num-3)
if max_num>3:
  for i in range(4,max_num+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for num in nums:
  print(dp[num])