import sys
from copy import deepcopy
input = sys.stdin.readline
n=int(input())
board=[]
for i in range(n):
  board.append(list(map(str,input().rstrip())))

ans=1

def search():
  global ans
  for i in range(n):
    cnt=1
    for j in range(n-1):
      if board[i][j]==board[i][j+1]:
        cnt+=1
        ans=max(ans,cnt)
      else:
        cnt=1

  for j in range(n):
    cnt=1
    for i in range(n-1):
      if board[i][j]==board[i+1][j]:
        cnt+=1
        ans=max(ans,cnt)
      else:
        cnt=1

search()

# 행끼리 교환
for i in range(n):
  for j in range(n-1):
    if board[i][j]!=board[i][j+1]:
      board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
      search()
      board[i][j],board[i][j+1]=board[i][j+1],board[i][j]

# 열끼리 교환
for i in range(n-1):
  for j in range(n):
    if board[i][j]!=board[i+1][j]:
      board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
      search()
      board[i][j],board[i+1][j]=board[i+1][j],board[i][j]

print(ans)