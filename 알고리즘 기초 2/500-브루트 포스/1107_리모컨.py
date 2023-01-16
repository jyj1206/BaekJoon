import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
button={0,1,2,3,4,5,6,7,8,9}
if m!=0:
  button-=set(list(map(int,input().split())))
ans=abs(100-n)

for num in range(1000001):
  num=str(num)
  for i in range(len(num)):
    if int(num[i]) not in button:
      break
    if i==len(num)-1:
      ans=min(ans,abs(int(num)-n)+len(num))

print(ans)

# 풀이 - 시간 초과
# case1=abs(100-n)
# case2=int(2e9)

# def func(num):
#   global case2
#   if len(str(n))+1<len(num):
#     return
#   if num:
#     if int(num)==0:
#       tmp=abs(int(num)-n)+1
#     else:
#       tmp=abs(int(num)-n)+len(num.lstrip('0'))
#     if case2>tmp:
#       case2=tmp

#   for i in button:
#     num=str(i)+num
#     func(num)
#     num=num[1:]

# func('')
# print(min(case1,case2))