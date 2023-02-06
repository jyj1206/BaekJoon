a, b = map(int,input().split())

if a==b:
  print(0)
else:
  if a>b:
    a,b = b,a
  print(b-a-1)
  print(*range(a+1,b))