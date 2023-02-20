import sys
input = sys.stdin.readline
n = int(input())

q = []

for _ in range(n):
  a, b = input().split()
  q.append((a, int(b)))

print(min(q, key = lambda x : x[1])[0])
