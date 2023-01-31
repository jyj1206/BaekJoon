import sys
input = sys.stdin.readline
n = int(input())
target = int(input())
board = [[0 for j in range(n)] for i in range(n)]

d = [(1,0),(0,1),(-1,0),(0,-1)]


i,j=0,0
board[i][j]=n*n
switch=0
ans=[1]*2
for k in range(n*n-1,0,-1):
  ni=i+d[switch%4][0]
  nj=j+d[switch%4][1]
  if 0<=ni<n and 0<=nj<n:
    if board[ni][nj]:
      switch+=1
      i+=d[switch%4][0]
      j+=d[switch%4][1]
    else:
      i=ni
      j=nj
  else:
    switch+=1
    i=i+d[switch%4][0]
    j=j+d[switch%4][1]
  board[i][j]=k
  if k==target:
    ans[0]=i+1
    ans[1]=j+1
    
for i in range(n):
  print(*board[i])
  
print(*ans)
