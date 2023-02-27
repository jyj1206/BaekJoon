import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  if 6 <= len(input().strip()) <= 9:
    print('yes')
  else:
    print('no')