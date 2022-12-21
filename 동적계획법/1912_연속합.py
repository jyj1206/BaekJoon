import sys
input = sys.stdin.readline

n=int(input())
number=list(map(int,input().split()))
dp=[0 for i in range(n)]

def func():
    max_val=-int(2e9)
    for i in range(0,n):
        for j in range(n-i):
            dp[j]=dp[j]+number[i+j]
            max_val=max(max_val,dp[j])
    return max_val


print(func())