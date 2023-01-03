import sys
input = sys.stdin.readline
t=int(input())

for i in range(t):
  words = list(input().strip().split())

  for word in words:
    stack=[]
    for char in word:
      stack.append(char)
    
    while stack:
      print(stack.pop(),end='')
      
    print(' ',end='')
  print()

# for i in range(t):
#   words = list(input().strip().split())
#   for word in words:
#     print(word[::-1], end=' ')
#   print()
