n = int(input())
dial=[300,60,10]
result=[]
for i in dial:
  temp=n//i
  result.append(temp)
  n-=temp*i

if n>0:
  print(-1)
else:
  print(*result)