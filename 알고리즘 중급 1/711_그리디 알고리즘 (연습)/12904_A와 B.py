import sys
input = sys.stdin.readline
s = list(input().strip())
t = list(input().strip())

reverse = False
while len(s)!=len(t):
  c = t.pop()
  
  if c == 'B':
    t = t[::-1]
  
if t == s:
  print(1)
else:
  print(0)