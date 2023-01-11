n=int(input())
ans=0
def func(nums):
  global ans
  if len(nums)>len(str(n)):
    return
  if nums:
    if int(nums)<=n:
      ans=max(ans,int(nums))
  for i in (4,7):
    nums=str(i)+nums
    func(nums)
    nums=nums[1:]

func('')
print(ans)