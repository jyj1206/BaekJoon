n = int(input())
s = input()
num = [int(input()) for _ in range(n)]
stack=[]

for char in s:
  if char =='+' :
    b,a =stack.pop(), stack.pop()
    stack.append(a+b)
  elif char =='-':
    b,a =stack.pop(), stack.pop()
    stack.append(a-b)
  elif char=='*':
    b,a =stack.pop(), stack.pop()
    stack.append(a*b)
  elif char=='/':
    b,a =stack.pop(), stack.pop()
    stack.append(a/b)
  else:
    stack.append(num[ord(char)-ord('A')])
print(f'{stack[-1]:.2f}')