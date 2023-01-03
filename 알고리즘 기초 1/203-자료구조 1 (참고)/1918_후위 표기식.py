n = input()
stack=[]
for c in n:
  if c.isupper():
    print(c,end='')
  else :
    if c=='(':
      stack.append(c)
    elif c==')':
      while stack[-1]!='(':
        print(stack.pop(),end='')
      stack.pop()
    elif c=='+' or c=='-':
      while stack and stack[-1]!='(':
        print(stack.pop(),end='')
      stack.append(c)
    # * or /
    else :
      while stack and (stack[-1]=='*' or stack[-1]=='/'):
        print(stack.pop(),end='')
      stack.append(c)


while stack :
  print(stack.pop(),end='')
