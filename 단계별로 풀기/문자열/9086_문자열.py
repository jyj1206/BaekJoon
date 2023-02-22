import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  s = input().strip()
  print(s[0] + s[-1])