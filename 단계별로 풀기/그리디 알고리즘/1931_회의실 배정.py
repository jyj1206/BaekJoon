import sys
input = sys.stdin.readline
n = int(input())

session = []
for i in range(n):
  s,f=map(int,input().split())
  session.append((s,f))
  
session.sort(key=lambda x :(x[1],x[0]))

last=0
cnt=0
for i in range(n):
  if session[i][0]>=last:
    last=session[i][1]
    cnt+=1
    
print(cnt)