s=input()
t=input()
result=[]

last=t[-1]
for char in s:
  result.append(char)
  if char==last and ''.join(result[-len(t):])==t:
    del result[-len(t):]



# for i in range(len(s)):
#   result.append(s[i])
  
#   if s[i]==last:
#     if len(result)>=len(t):
#       for j in range(len(t)):
#         if result[-(len(t))+j]!=t[j]:
#           break
#       else:
#         for j in range(len(t)):
#           result.pop()
  
if not result:
  print('FRULA')
else:
  print(''.join(result))