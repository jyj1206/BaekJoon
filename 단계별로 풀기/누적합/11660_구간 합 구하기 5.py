import sys 
input = sys.stdin.readline
n, m = map(int,input().split())
table=[[0 for i in range(n+1)]]
for i in range(n):
  table.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(1,n+1):
    table[i][j]+=table[i-1][j]+table[i][j-1]-table[i-1][j-1]

for i in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  print(table[x2][y2]-table[x2][y1-1]-table[x1-1][y2]+table[x1-1][y1-1])