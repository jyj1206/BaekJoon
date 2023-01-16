n, m = map(int,input().split())
table = [list(map(int,input())) for i in range(n)]

ans=0
for i in range(1<<n*m):
  #가로로 자른 종이 확인
  total_row_sum=0
  for row in range(n):
    row_sum=0
    for col in range(m):
      idx = row*m+col
      if i&(1<<idx) !=0:
        row_sum=row_sum*10+table[row][col]
      else:
        total_row_sum+=row_sum
        row_sum=0
    total_row_sum+=row_sum
  
  #세로로 자른 종이 확인
  total_col_sum=0
  for col in range(m):
    col_sum=0
    for row in range(n):
      idx = row*m+col
      if i&(1<<idx)==0:
        col_sum=col_sum*10+table[row][col]
      else:
        total_col_sum+=col_sum
        col_sum=0
    total_col_sum+=col_sum

  ans=max(ans,total_row_sum+total_col_sum)
  
print(ans)