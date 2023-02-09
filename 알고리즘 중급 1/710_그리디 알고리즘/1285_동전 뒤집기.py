import sys
input = sys.stdin.readline
n = int(input())
coins = [list(input().strip()) for _ in range(n)]

flip = {'H' : 'T', 'T' : 'H'}

def change_row(temp, j):
  for i in range(n):
    temp[j][i] = flip[temp[j][i]]

def count(temp):
  t_cnt=0
  for i in range(n):
    for j in range(n):
      if temp[i][j] == 'T':
        t_cnt+=1
  return t_cnt

ans = n*n
for i in range(1 << n):
  temp = [coin[:] for coin in coins]
  for j in range(n):
    if i & 1 << j:
      change_row(temp, j)
      
  r_cnt = 0
  for i in range(n):
    t_cnt = 0
    for j in range(n):
      if temp[j][i] == 'T':
        t_cnt += 1
    r_cnt += min(t_cnt, n - t_cnt)
  ans = min(ans, r_cnt)

print(ans)