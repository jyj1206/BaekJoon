n, m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
result=[]

def func(depth):
  if depth==m:
    print(*result)
    return
  
  prev=0
  for i in range(n):
    if prev!=nums[i]:
      result.append(nums[i])
      prev=nums[i]
      func(depth+1)
      result.pop()

func(0)