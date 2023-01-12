n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result=[]
visited=[False]*n

def func(start):
  if len(result)==m:
    print(*result)
    return
  
  for i in range(start,n):
    if not visited[i]:
      visited[i]=True
      result.append(nums[i])
      func(i+1)
      result.pop()
      visited[i]=False

func(0)