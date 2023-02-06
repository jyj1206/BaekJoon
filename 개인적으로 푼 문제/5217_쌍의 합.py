t = int(input())
for _ in range(t):
  n = int(input())
  ans=[]
  for i in range(1,n//2+1):
    if i==n-i:
      continue
    ans.append(f'{i} {n-i}')
  print(f'Pairs for {n}: {", ".join(ans)}')
