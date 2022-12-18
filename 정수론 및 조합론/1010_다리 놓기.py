import sys
input = sys.stdin.readline
n = int(input())
dp = []
for i in range(0,31):
    temp=[]
    for j in range(i+1):
        if i==j:
            temp.append(1)
        elif j==1:
            temp.append(i)
        elif j==0:
            temp.append(1)
        else : temp.append(dp[i-1][j-1]+dp[i-1][j])
    dp.append(temp)

for i in range(n):
    A, B = map(int,input().split())
    print(dp[B][A])
    