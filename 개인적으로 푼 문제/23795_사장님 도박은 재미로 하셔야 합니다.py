import sys
input = sys.stdin.readline
result = 0
while True:
  n = int(input())
  if n == -1:
    break
  result += n

print(result)
