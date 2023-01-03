t = int(input())
nums=[int(input()) for _ in range(t)]
max_num=max(nums)
prime = [False,False]+[True]*(max_num-1)
for i in range(2,int(max_num**(0.5))+1):
  if prime[i]:
    for j in range(i+i,max_num+1,i):
      prime[j]=False

for num in nums:
  ans=0
  for i in range(2,num//2+1):
    if prime[i] and prime[num-i]:
      ans+=1
  print(ans)





# 개선전
# max_num=1000001
# prime = [False,False]+[True]*(max_num-2)

# for i in range(max_num):
#   if prime[i]:
#     for j in range(i+i,max_num,i):
#       prime[j]=False

# for i in range(t):
#   n= int(input())
#   ans=0
#   for j in range(2,n//2+1):
#     if prime[j] and prime[n-j]:
#       ans+=1
#   print(ans)