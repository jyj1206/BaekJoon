import sys
input = sys.stdin.readline
check = [False]*2001
n = int(input())
num = list(map(int,input().split()))

print(*sorted(set(num)))


# 계수 정렬
# min_num=min(num)
# max_num=max(num)

# for i in range(n):
#   check[num[i]-min_num]=True

# for i in range(max_num-min_num+1):
#   if check[i]:
#     print(i+min_num,end=' ')