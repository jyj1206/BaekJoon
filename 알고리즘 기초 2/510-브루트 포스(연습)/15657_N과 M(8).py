n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result=[]

def func(start):
  if len(result)==m:
    print(*result)
    return
  
  for i in range(start,n):
    result.append(nums[i])
    func(i)
    result.pop()

func(0)


