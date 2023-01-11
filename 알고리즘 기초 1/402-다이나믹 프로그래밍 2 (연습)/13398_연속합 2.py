n=int(input())
num = list(map(int,input().split()))
dp = [[0 for j in range(n)] for i in range(2)]

dp[0][0]=num[0]

ans=num[0]
for i in range(1,n):
  # n-1까지의 연속합에 현재 i번째 숫자를 더한 것과 현재 i 번째 숫자 값 비교 -> 현재 i번째 숫자가 더 큰 경우 i번쨰부터 연속합 다시시작
  dp[0][i]=max(dp[0][i-1]+num[i],num[i])

  # 앞에서 연속합을 구할때 아무것도 제거하지 않은 경우에 i 번째를 제거하는 것과 i번쨰 이전에서 이미 특정 원소를 제거하여 현재 i값 더해주는 경우
  dp[1][i]=max(dp[0][i-1],dp[1][i-1]+num[i])
  
  ans=max(ans,dp[0][i],dp[1][i])

print(ans)