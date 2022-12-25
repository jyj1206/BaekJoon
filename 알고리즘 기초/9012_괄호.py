import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
  string=input().strip()
  stack=[]
  left=0
  for char in string:
    if char=='(':
      stack.append('(')
    else:
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  else:
    if stack: print('NO')
    else : print('YES')
        
# for i in range(t):
#   string=input().strip()
#   stack=list(map(str,string))
#   left = 0
#   while stack and left>=0:
#     if stack.pop(0)=='(':
#       left+=1
#     else:
#       left-=1
  
#   if not stack and left==0:
#     print('YES')
#   else:
#     print('NO')