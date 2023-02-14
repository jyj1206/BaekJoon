import sys
input = sys.stdin.readline
n = int(input())
num = []
for _ in range(n):
  num.append(int(input()))

num.sort(reverse=True)

ans = 0
for i in range(n):
  ans = max(ans, num[i]*(i+1))

print(ans)