n=int(input())
s=input().split()
ans=[]
visited=[0]*10

def func(prev,cnt,result):
  if cnt==n:
    p=''.join(map(str,result))
    ans.append(int(p))
    return
  
  if s[cnt]=='<':
    for i in range(prev+1,10):
      if visited[i]==0:
        visited[i]=1
        result.append(i)
        func(i,cnt+1,result)
        result.pop()
        visited[i]=0
  else:
    for i in range(prev):
      if visited[i]==0:
        visited[i]=1
        result.append(i)
        func(i,cnt+1,result)
        result.pop()
        visited[i]=0

for i in range(10):
  visited[i]=1
  func(i,0,[i])
  visited[i]=0

print(max(ans))
print(str(min(ans)).zfill(n+1))