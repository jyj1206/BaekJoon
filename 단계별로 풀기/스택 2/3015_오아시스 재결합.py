# 풀이 한번 보자
import sys
input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
  h.append(int(input()))

ans = 0

stack = []
for i in range(n):
  check = 1
  while stack and stack[-1] < h[i]:
    # 현재 들어온 거랑 크기를 비교
    ans += 1
    pop_h = stack.pop()
    
    if stack and stack[-1] >= pop_h:
      ans += check
    # 현재 pop 한거랑 stack에 top과 비교했을때 같으면 다음에 1을 더해서 뺌
    if stack and stack[-1] == pop_h:
      check += 1
    else:
      check = 1
  stack.append(h[i])

check = 1
while stack:
  pop_h = stack.pop()
  
  if stack and stack[-1] >= pop_h:
    ans += check
  
  if stack and stack[-1] == pop_h:
    check += 1
  else:
    check = 1

print(ans)