n=int(input())
if n%2==1:
  print(0)
else:
  dp=[0]+[0 for i in range(n//2)]
  dp[1]=3
  for i in range(2,n//2+1):
    #dp[i]=3*dp[i-1]+2*sum(dp[:i-1])+2
    
    dp[i]=3*dp[i-1]+2
    for j in range(i-1):
      dp[i]+=2*dp[j]
  print(dp[-1])