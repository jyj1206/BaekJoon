import sys
input = sys.stdin.readline
l = int(input())
for _ in range(l):
  n, x = input().split()
  print(x * int(n))