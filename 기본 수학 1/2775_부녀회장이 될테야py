# 동적계획법 top-down(하향식 접근)
# def func(a,b):
#     global whole_floor
#     if b==0:
#         return 0
#     if whole_floor[a][b]!=0:
#         return whole_floor[a][b]
#     whole_floor[a][b]=func(a-1,b)+func(a,b-1)
#     return whole_floor[a][b]
    
#t=int(input())
# for i in range(t):
#     a=int(input())
#     b=int(input())
#     whole_floor=[[0 for i in range(b+1)]for i in range(a+1)]
    
#     for i in range(b+1):
#         whole_floor[0][i]=i
#     print(func(a,b))
import sys

T = int(sys.stdin.readline())

for i in range(T):
    dp = [j for j in range(1, 15)]
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    for l in range(k):
        for m in range(1, n):
            dp[m] = dp[m-1] + dp[m]
    
    print(dp[n-1])


# floor=[i for i in range(b+1)]

# for i in range(a):
#     temp=[]
#     for i in range(b+1):
#         temp.append(sum(floor[:i+1]))
#     floor=temp.copy()
#     print(floor)

# print(floor[-1])
