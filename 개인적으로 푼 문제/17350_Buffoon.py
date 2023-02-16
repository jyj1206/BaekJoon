import sys
input = sys.stdin.readline
n = int(input())
candidate = []
for i in range(n):
  candidate.append(int(input()))

if max(candidate) == candidate[0]:
  print("S")
else:
  print("N")