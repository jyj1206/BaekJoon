n=int(input())
dp=[0 for i in range(n+1)]
def func(n):
    if dp[n]!=0:
        return dp[n]
    if n==1:
        dp[n]=0
    else :
        dp[n]=func(n-1)+1
        if n%3==0:
            dp[n]=min(dp[n],func(n//3)+1)
        if n%2==0:
            dp[n]=min(dp[n],func(n//2)+1)
    return dp[n]
func(n)
print(dp[-1])

# if n==1 or n==2:
#     print(n-1)
# else:
#     dp[1]=0
#     dp[2]=1
#     for i in range(3,n+1):
#         dp[i]=dp[i-1]+1
#         if i%3==0:
#             dp[i]=min(dp[i],dp[i//3]+1)
#         if i%2==0:
#             dp[i]=min(dp[i],dp[i//2]+1)
#     print(dp[n])