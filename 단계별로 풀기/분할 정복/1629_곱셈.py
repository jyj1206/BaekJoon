import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

# 재귀 사용
# def fpow(C,n):
#   if n==1:
#     return C%c
#   else:
#     x = fpow(C,n//2)
#     if n%2==0:
#       return (x*x)%c
#     else:
#       return (x*x*C)%c


# 반복문 사용
def fpow(C,n):
  res=1
  while n:
    if n%2==1:
      res=(res*C)%c
    C=(C*C)%c
    n//=2
  return res

print(fpow(a,b))