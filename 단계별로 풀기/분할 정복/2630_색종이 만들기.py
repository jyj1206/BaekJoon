import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
paper = [list(map(int,input().split())) for i in range(N)]

blue_cnt=0
white_cnt=0
def dq(cur_x,cur_y,n):
  global blue_cnt, white_cnt
  
  if n==1:
    if paper[cur_x][cur_y]==1:
      blue_cnt+=1
    else:
      white_cnt+=1
  return

  blue=0
  white=0
  total=n*n
  for i in range(cur_x,cur_x+n):
    for j in range(cur_y,cur_y+n):
      if paper[i][j]==0:
        white+=1
      else:
        blue+=1
        
  if total==blue:
    blue_cnt+=1
    return
  if total==white:
    white_cnt+=1
    return
  
  n=n//2
  dq(cur_x,cur_y,n)
  dq(cur_x,cur_y+n,n)
  dq(cur_x+n,cur_y,n)
  dq(cur_x+n,cur_y+n,n)

dq(0,0,N)
print(white_cnt)
print(blue_cnt)