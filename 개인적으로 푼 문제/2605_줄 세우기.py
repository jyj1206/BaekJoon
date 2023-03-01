import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

a = []
for i in range(n):
  a.insert(i - data[i], i + 1)

print(*a)