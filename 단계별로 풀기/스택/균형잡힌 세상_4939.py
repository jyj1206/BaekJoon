import sys
while(True):
  s = sys.stdin.readline().rstrip()
  if s=='.':
    break
  stack=[]
  
  for char in s:
    if char == '.':
      if not stack:
        print('yes')
      else:
        print('no')
      break
    elif char=='(':
      stack.append(')')
    elif char==')':
      if not stack or stack.pop()!=char:
        print('no')
        break
    elif char=='[':
      stack.append(']')
    elif char==']':
      if not stack or stack.pop()!=char:
        print('no')
        break