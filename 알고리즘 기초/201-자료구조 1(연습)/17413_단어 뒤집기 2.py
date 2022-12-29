import sys
s = sys.stdin.readline().rstrip()
result=[]
stack=[]

i=0
while(i!=len(s)):
  if s[i]=='<':
    while stack:
      result.append(stack.pop())
    while s[i]!='>':
      result.append(s[i])
      i+=1
    result.append('>')
  elif s[i]==' ':
    while stack:
      result.append(stack.pop())
    result.append(s[i])
  else :
    stack.append(s[i])
  i+=1
while stack:
  result.append(stack.pop())

print(''.join(result))