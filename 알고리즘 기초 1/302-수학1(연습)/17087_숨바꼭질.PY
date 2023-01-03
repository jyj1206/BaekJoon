import math
n,s =map(int,input().split())
a = list(map(int,input().split()))

ans=abs(s-a[0])
if n==1:
  print(ans)
else:
  for i in range(1,n):
    ans = math.gcd(ans,s-a[i])
  print(ans)

