from math import lcm
num = list(map(int,input().split()))

ans=int(2e9)
for i in range(5):
  for j in range(5):
    for k in range(5):
      if i!=j and j!=k and i!=k:
        ans=min(ans,lcm(lcm(num[i],num[j]),num[k]))
print(ans)

#num.sort()
#least = num[2]
# while(True):
#   cnt=0
#   for i in range(5):
#     if least%num[i]==0:
#       cnt+=1
#   if cnt>=3:
#     print(least)
#     break
#   least+=1
