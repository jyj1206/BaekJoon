n=int(input())
a=[0]+list(map(int,input().split()))
dp=[1]*(n+1)

for i in range(1,n+1):
  for j in range(1,i):
    if a[i]>a[j]:
      dp[i]=max(dp[i],dp[j]+1)

m=max(dp)
print(m)
ans=[]
for i in range(n,-1,-1):
  if dp[i]==m:
    ans.append(a[i])
    m-=1
  if m==0:
    break

print(' '.join(map(str,reversed(ans))))

