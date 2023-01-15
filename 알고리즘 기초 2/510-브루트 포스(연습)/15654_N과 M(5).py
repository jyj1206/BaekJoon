n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited=[False]*n
result=[]

def func(depth):
  if depth==m:
    print(' '.join(map(str,result)))
    return
  
  for i in range(n):
    if not visited[i]:
      visited[i]=True
      result.append(nums[i])
      func(depth+1)
      result.pop()
      visited[i]=False

func(0)