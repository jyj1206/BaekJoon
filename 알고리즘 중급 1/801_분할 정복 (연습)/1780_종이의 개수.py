import sys
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

ans = {-1 : 0, 0 : 0, 1 : 0}
def dq(i, j, n):
  s = paper[i][j]
  if n == 1:
    ans[s]+=1
    return
  for x in range(i, i+n):
    for y in range(j, j+n):
      if s != paper[x][y] :
        next_n = n // 3
        for k in range(i, i+n, next_n):
          for l in range(j, j+n, next_n):
            dq(k, l, next_n)
        return
  ans[s] += 1

dq(0, 0, n)
print(ans[-1])
print(ans[0])
print(ans[1])