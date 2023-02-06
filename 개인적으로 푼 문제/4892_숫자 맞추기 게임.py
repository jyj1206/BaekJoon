import sys
input = sys.stdin.readline
i=1
while True:
  n=int(input())
  if n==0:
    break
  print(f'{i}. {"even" if n%2==0 else "odd"} {(n*3+1)//2//3}')
  i+=1