import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()

e = s.count('e')
two = n - e

if e > two :
  print('e')
elif e < two:
  print(2)
else:
  print('yee')
