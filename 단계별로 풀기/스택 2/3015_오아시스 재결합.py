# 다시 풀기
import sys
input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
  h.append(int(input()))

ans = 0

# 연속으로 같은 키의 사람 처리
d = 0
for i in range(1, n):
  if h[i] == h[i-1]:  d += 1
  else: d = 0
  
  if d > 0: ans += d

stack = []

for i in range(n):
  while stack and stack[-1] < h[i]:
    stack.pop()
    ans += 1
  
  stack.append(h[i])

stack = []
for i in range(n - 1, -1 , -1):
  while stack and stack[-1] < h[i]:
    stack.pop()
    ans += 1
  
  stack.append(h[i])

print(ans)