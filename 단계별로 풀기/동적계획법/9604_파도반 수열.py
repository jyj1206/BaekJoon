import sys
input =sys.stdin.readline
t= int(input())
def func(n):
    dp = [1,1,1]+[0]*(n-3)
    for i in range(3,n):
        dp[i]=dp[i-2]+dp[i-3]
    return dp[n-1]

for i in range(t):
    n=int(input())
    print(func(n))
