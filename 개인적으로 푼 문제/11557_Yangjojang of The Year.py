t=int(input())
for i in range(t):
  n=int(input())
  s=[]
  for i in range(n):
    s.append(input().split())
  s.sort(key=lambda x: int(x[1]))
  print(s[-1][0])