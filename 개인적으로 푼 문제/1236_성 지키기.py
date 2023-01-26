import sys
input = sys.stdin.readline

n,m = map(int,input().split())

floor=[list(input().strip()) for i in range(n)]

# 풀이 1
flag_row=[False]*n
flag_col=[False]*m

for i in range(n):
  for j in range(m):
    if floor[i][j]=='X':
      flag_row[i]=True
      flag_col[j]=True

print(max(flag_row.count(False),flag_col.count(False)))





# 풀이 2
# col_cnt=0
# for i in range(n):
#   cnt=1
#   for j in range(m):
#     if floor[i][j]=='X':
#       cnt=0
#       break
#   col_cnt+=cnt
  
# row_cnt=0
# for j in range(m):
#   cnt=1
#   for i in range(n):
#     if floor[i][j]=='X':
#       cnt=0
#       break
#   row_cnt+=cnt
  
# print(max(col_cnt,row_cnt))