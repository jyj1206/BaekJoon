n, m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
result=[]
visited=[False]*n

def func(start):
  if len(result)==m:
    print(*result)
    return
  
  prev=0
  for i in range(start,n):
    if prev!=nums[i] and not visited[i]:
      result.append(nums[i])
      visited[i]=True
      prev=nums[i]
      func(i+1)
      result.pop()
      visited[i]=False

func(0)