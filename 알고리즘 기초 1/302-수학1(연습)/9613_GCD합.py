import sys, math
input = sys.stdin.readline
t= int(input())
for i in range(t):
  ans=0
  nums=list(map(int,input().split()))
  for i in range(1,len(nums)):
    for j in range(i+1,len(nums)):
      ans+=math.gcd(nums[i],nums[j])
  print(ans)