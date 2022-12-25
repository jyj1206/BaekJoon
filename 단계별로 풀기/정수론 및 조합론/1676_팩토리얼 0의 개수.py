import math
n=int(input())

## 풀이 1
#n=math.factorial(n)
# def count_0(count,n):
#     if n%10==0:
#         count+=1
#         return count_0(count,n//10)
#     else :
#         return count
# cnt=count_0(0,n)
# print(cnt)

# 풀이 2
cnt=0
while n>0:
    cnt+=n//5
    n//=5
print(cnt)
