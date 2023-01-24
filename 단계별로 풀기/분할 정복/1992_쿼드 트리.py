import sys
input = sys.stdin.readline
N = int(input())
screen = [list(map(int,input().strip())) for i in range(N)]

result=[]
def dq(i,j,n):
  color=screen[i][j]
  if n==1:
    result.append(color)
    return
  for x in range(i,i+n):
    for y in range(j,j+n):
      if color!= screen[x][y]:
        result.append('(')
        dq(i,j,n//2)
        dq(i,j+n//2,n//2)
        dq(i+n//2,j,n//2)
        dq(i+n//2,j+n//2,n//2)
        result.append(')')
        return
  
  result.append(color)
  
dq(0,0,N)

print(''.join(map(str,result)))