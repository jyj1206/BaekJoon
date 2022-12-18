import math
n, k = map(int,input().split())

# 1번 풀이 - 필요없는 공간이 생김
# dp=[[0 for j in range(k+1)] for i in range(n+1)]
# for i in range(0,n+1):
#     for j in range(0,k+1):
#         if i==j:
#             dp[i][j]=1
#         elif j==0:
#             dp[i][j]=1
#         elif j==1:
#             dp[i][j]=i
#         else:
#             dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

# 2번 풀이 - 파스칼 삼각형
dp=[]
for i in range(0,n+1):
    temp=[]
    for j in range(0,i+1):
        if i==j:
            temp.append(1)
        elif j==0:
            temp.append(1)
        elif j==1:
            temp.append(i)
        else:
            temp.append(dp[i-1][j-1]+dp[i-1][j])
    dp.append(temp)
print(dp[n][k]%10007)

# 3번 풀이 
#print((math.factorial(n)//(math.factorial(n-k)*math.factorial(k)))%10007)
