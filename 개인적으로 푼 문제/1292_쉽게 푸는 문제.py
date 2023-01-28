import sys
input = sys.stdin.readline
a,b = map(int,input().split())
s=[0]
for i in range(1,b+1):
  if len(s)>1000:
    break
  for j in range(i):
    s.append(i)

print(sum(s[a:b+1]))