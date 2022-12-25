import sys
input = sys.stdin.readline
n = int(input())
j=1
stack=[]
ans=[]
for i in range(n):
  s = int(input())
  while j<=s:
    stack.append(j)
    ans.append('+')
    j+=1

  if stack[-1]==s:
    stack.pop()
    ans.append('-')
  else :
    print('NO')
    break
else:
  for oper in ans:
    print(oper)

# sequence =[int(input()) for i in range(n)]

# stack=[]
# j=0
# result=[]
# for i in range(1,n+1):
#   stack.append(i)
#   result.append('+')
#   while stack[-1]==sequence[j]:
#     stack.pop()
#     result.append('-')
#     j+=1
#     if not stack:
#       break
  
# if stack:
#   print('NO')
# else:
#   for oper in result:
#     print(oper)