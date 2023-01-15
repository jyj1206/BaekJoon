import sys
n=int(input())
nums=list(map(int,input().split()))

if sorted(nums,reverse=True)==nums:
  print(-1)
else:
  for i in range(n-1,-1,-1):
    if nums[i]>nums[i-1]:
      x=i-1
      break
  
  for i in range(n-1,-1,-1):
    if nums[i]>nums[x]:
      y=i
      break
  
  nums[x],nums[y]=nums[y],nums[x]
  nums[x+1:]=sorted(nums[x+1:])
  print(*nums)