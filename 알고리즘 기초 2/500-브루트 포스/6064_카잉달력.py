import sys
input = sys.stdin.readline
t=int(input())
for i in range(t):
  m,n,x,y=map(int,input().split())
  while x<=m*n:
    if x%n==y%n:
      print(x)
      break
    x+=m
  else:
    print(-1)
