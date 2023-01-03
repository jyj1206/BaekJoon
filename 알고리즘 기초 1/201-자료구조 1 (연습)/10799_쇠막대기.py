import sys
s = sys.stdin.readline().strip()
stack=[]
sum=0
for i in range(len(s)):
  if s[i]==')':
    stack.pop()
    if s[i-1]==')':
      sum+=1
    else:
      sum+=len(stack)
  else: 
    stack.append(s[i])

print(sum)