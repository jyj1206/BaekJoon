n = input().split('-')
num=[]

for i in n:
  sum=0
  s=i.split('+')
  for j in s:
    sum+=int(j)
  num.append(sum)
  
ans=num[0]
for i in range(1,len(num)):
  ans-=num[i]

print(ans)