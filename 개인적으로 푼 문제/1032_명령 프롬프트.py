n=int(input())
result=list(input())
for i in range(n-1):
  comp=input()
  for i in range(len(result)):
    if comp[i]!=result[i]:
      result[i]='?'
      
print(''.join(result))