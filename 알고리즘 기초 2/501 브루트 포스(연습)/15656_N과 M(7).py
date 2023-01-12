n, m = map(int,input().split())
nums= list(map(int,input().split()))
nums.sort()
result=[]

def func(depth):
  if depth==m:
    print(*result)
    return
  
  for i in range(n):
    result.append(nums[i])
    func(depth+1)
    result.pop()

func(0)