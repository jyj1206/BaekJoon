import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int,input().split()))

num=1
for i in sorted(s):
    if num<i:
        break
    num+=i
print(num)



# dfs 풀이
# visited = [0]*10000000
# def dfs(idx,sum) :
#     if idx == n :
#       return
#     sum += s[idx]
#     visited[sum] = 1
#     dfs(idx+1, sum)
#     dfs(idx+1, sum-s[idx])

# dfs(0,0)
# print(visited[1:].index(0)+1)

# 비트 마스크 
# ans = set()
# for i in range(1,1<<n):
#   sum=0
#   for j in range(n):
#     if i&(1<<j):
#       sum+=s[j]
#   ans.add(sum)

# i=1
# while i in ans:
#   i+=1
# print(i)
