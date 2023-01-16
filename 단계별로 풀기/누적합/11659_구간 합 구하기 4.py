import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums=[0]+list(map(int,input().split()))

for i in range(1,n+1):
  nums[i]+=nums[i-1]

for i in range(m):
  a, b = map(int,input().split())
  print(nums[b]-nums[a-1])