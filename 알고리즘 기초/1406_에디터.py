import sys
input = sys.stdin.readline
stack1 = list(map(str,input().strip()))
m = int(input())
stack2 = []
for i in range(m):
  order = input().split()
  if order[0]=='L':
    if stack1:
      char=stack1.pop()
      stack2.append(char)
  elif order[0]=='D':
    if stack2:
      char=stack2.pop()
      stack1.append(char)
  elif order[0]=='B':
    if stack1:
      stack1.pop()
  else:
    stack1.append(order[1])

stack1.extend(reversed(stack2))

print(''.join(stack1))




# 시간 초과 deque : insert, del O(n)
# import sys
# from collections import deque
# input = sys.stdin.readline
# s = input().strip()
# m = int(input())
# _deque=deque(map(str,s))

# l = len(_deque)
# for i in range(m):
#   order = input().split()
#   if order[0]=='L':
#     if l!=0:
#       l-=1
#   elif order[0]=='D':
#     if l!=len(_deque):
#       l+=1
#   elif order[0]=='B':
#     if l!=0:
#       del _deque[l-1]
#       l-=1
#   else:
#     _deque.insert(l,order[1])
#     l+=1

# for char in _deque:
#   print(char, end='')