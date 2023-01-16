n,k = map(int,input().split())
nums = [0]+list(map(int,input().split()))

for i in range(n+1):
  nums[i]+=nums[i-1]

max_temp=-int(2e9)
for i in range(k,n+1):
  max_temp=max(max_temp,nums[i]-nums[i-k])

print(max_temp)
