import sys
input = sys.stdin.readline
t = int(input())
total=[0,0]
for i in range(t):
  for i in range(9):
    y,k=map(int,input().split())
    total[0]+=y
    total[1]+=k
    
  if total[0]>total[1]:
    print('Yonsei')
  elif total[0]==total[1]:
    print('Draw')
  else:
    print('Korea')