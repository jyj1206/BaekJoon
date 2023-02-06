# 다시 풀기
import sys
input = sys.stdin.readline
n = int(input())
p = [int(input()) for _ in range(n)]

stack = []
ans=0
for i, cur_h in enumerate(p):
  while stack and stack[-1][0]<cur_h:
    h, idx =stack.pop()
    