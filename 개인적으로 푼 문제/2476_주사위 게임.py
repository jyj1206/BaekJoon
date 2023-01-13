t = int(input())

ans=0
for i in range(t):
  a,b,c = map(int,input().split())
  
  if a==b and b==c and c==a:
    ans = max(ans,10000+a*1000)
  elif a==b :
    ans = max(ans,1000+a*100)
  elif b==c :
    ans = max(ans,1000+b*100)
  elif c==a :
    ans = max(ans,1000+c*100)
  else:
    ans = max(ans,max(a,b,c)*100)
    
print(ans)