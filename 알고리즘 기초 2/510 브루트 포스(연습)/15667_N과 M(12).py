n, m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
result=[]

def func(start):
  if len(result)==m:
    print(*result)
    return
  
  prev=0
  for i in range(start,n):
    if prev!=nums[i]:
      result.append(nums[i])
      prev=nums[i]
      func(i)
      result.pop()

func(0)