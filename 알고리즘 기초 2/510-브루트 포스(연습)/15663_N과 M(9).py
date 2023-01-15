n,m = map(int,input().split())
nums = list(map(int,input().split()))
result=[]
nums.sort()
visited=[False]*n

def func(depth):
  if depth==m:
    print(*result)
    return
  prev=0
  for i in range(n):
    if nums[i]!=prev and not visited[i]:
      result.append(nums[i])
      visited[i]=True
      prev=nums[i]
      func(depth+1)
      visited[i]=False
      result.pop()

func(0)







# 해쉬
# n,m = map(int,input().split())
# nums = list(map(int,input().split()))
# result=[]
# nums.sort()
# visited=[False]*n
# ans={}

# def func(depth):
#   if depth==m:
#     s=' '.join(map(str,result))
#     if s not in ans:
#       ans[s]=1
#       print(s)
#     return

#   for i in range(n):
#     if not visited[i]:
#       result.append(nums[i])
#       visited[i]=True
#       func(depth+1)
#       visited[i]=False
#       result.pop()

# func(0)


# Counter 이용
# from collections import Counter
# n,m = map(int,input().split())
# nums = list(map(int,input().split()))
# cnt=Counter(nums)
# nums=sorted(list(set(nums)))
# result=[]

# def func(depth):
#   if depth==m:
#     print(*result)
#     return

#   for num in nums:
#     if cnt[num]!=0:
#       result.append(num)
#       cnt[num]-=1
#       func(depth+1)
#       cnt[num]+=1
#       result.pop()

# func(0)