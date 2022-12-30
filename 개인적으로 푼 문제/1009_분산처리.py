import sys
input = sys.stdin.readline
test=int(input())
for i in range(test):
  a,b = map(int,input().split())
  a%=10
  if a==0:
    print(10)
  elif a in [1,5,6]:
    print(a)
  elif a in [4,9]:
    print(a*a%10 if b%2==0 else a)
  else:
    if b%4==0:
      print((a**4)%10)
    else:
      print((a**(b%4))%10)