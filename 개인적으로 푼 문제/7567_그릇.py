bowls=input()
ans=0

for i in range(len(bowls)):
  if i==0:
    ans+=10
  elif bowls[i-1] != bowls[i]:
    ans+=10
  else:
    ans+=5
    
print(ans)