n = int(input())
ans =''
if n==0:
  print(0)
else:
  while(n!=0):
    if n%-2:
      ans='1'+ans
      n=n//-2+1
    else:
      ans='0'+ans
      n//=-2
  print(ans)