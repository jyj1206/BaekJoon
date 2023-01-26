import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int,input().split()))
total_y=0
total_m=0
for s in h:
  y = (s//30+1)*10
  m = (s//60+1)*15
  total_y+=y
  total_m+=m
  
if total_y<total_m:
  print(f'Y {total_y}')
elif total_y>total_m:
  print(f'M {total_m}')
else:
  print(f'Y M {total_m}')