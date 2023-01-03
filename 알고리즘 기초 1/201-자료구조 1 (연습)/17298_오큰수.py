import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
stack=[]
result=[-1 for i in range(n)]

for i in range(n):
  while stack and a[i]>a[stack[-1]]:
    idx=stack.pop()
    result[idx]=a[i]
  stack.append(i)

print(' '.join(map(str,result)))

# 내풀이
# stack.append(a.pop())
# result[-1]=-1

# for i in range(n-2,-1,-1):
#   while stack:
#     compare=stack.pop()
#     if compare>a[i]:
#         result[i]=compare
#         stack.append(compare)
#         stack.append(a[i])
#         break
#   else:
#     stack.append(a[i])
#     result[i]=-1


# print(' '.join(map(str,result)))
