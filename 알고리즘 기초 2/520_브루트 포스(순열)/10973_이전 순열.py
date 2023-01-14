import sys
input = sys.stdin.readline
n = int(input())
nums=list(map(int,input().split()))

if sorted(nums)==nums:
  print(-1)
else:
  for i in range(n-1,-1,-1):
    if nums[i-1]>nums[i]:
      x=i-1
      break
  for i in range(n-1,-1,-1):
    if nums[x]>nums[i]:
      y=i
      break
  nums[x],nums[y]=nums[y],nums[x]
  nums[x+1:]=sorted(nums[x+1:],reverse=True)
  print(*nums)