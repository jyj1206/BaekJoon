import sys
input = sys.stdin.readline
n= int(input())
step=[]

for i in range(n):
    step.append(int(input()))

dp=[0 for i in range(n)]
if len(step)<=2:
    print(sum(step))
else :
    dp[0]=step[0]
    dp[1]=step[0]+step[1]
    dp[2]=step[2]+max(step[0],step[1])
    for i in range(3,n):
        dp[i]=step[i]+max(dp[i-3]+step[i-1],dp[i-2])
    print(dp[-1])





# # 공간 낭비가 너무 많음
# dp=[[0,0,0]]
# for i in range(n):
#     step=int(input())
#     dp.append([0,step,step])

# for i in range(2,n+1):
#     dp[i][1]+=dp[i-2][2]
#     dp[i][2]+=max(dp[i-1][1],dp[i-2][2])

# if n==1:
#     print(dp[1][1])
# elif n==2:
#     print(dp[2][1]+dp[1][1])
# else:
#     print(max(dp[n]))