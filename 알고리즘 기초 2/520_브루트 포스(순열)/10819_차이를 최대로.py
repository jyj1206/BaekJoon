from itertools import permutations
n=int(input())
nums=list(map(int,input().split()))
ans=-int(2e9)

for p in permutations(nums):
  sum=0
  for i in range(n-1):
    sum+=abs(p[i]-p[i+1])
  ans=max(ans,sum)
print(ans)