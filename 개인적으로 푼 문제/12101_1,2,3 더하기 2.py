n,k=map(int,input().split())

num=[1,2,3]
result=[]
def func(sum,ans):
  if sum==n:
    result.append('+'.join(map(str,ans)))
    return

  for j in num:
    if sum+j<=n:
      sum+=j
      ans.append(j)
      func(sum,ans)
      ans.pop()
      sum-=j
func(0,[])

if len(result)<k:
  print(-1)
else:
  print(result[k-1])