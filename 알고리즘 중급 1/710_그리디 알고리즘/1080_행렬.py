import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a = [list(map(int,input().strip())) for _ in range(n)]
b = [list(map(int,input().strip())) for _ in range(n)]

def change(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      a[i][j] = 1 - a[i][j]

cnt = 0
for i in range((n-3)+1):
  for j in range((m-3)+1):
    if a[i][j] != b[i][j]:
      cnt += 1
      change(i, j)

if a==b:
  print(cnt)
else:
  print(-1)