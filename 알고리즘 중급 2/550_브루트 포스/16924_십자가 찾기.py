import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
result = [['.'] * m for _ in range(n)]
# 상 하 좌 우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def cross(d, cnt):
  
  for i in range(4):
    d[i][0] += move[i][0]
    d[i][1] += move[i][1]
    if d[i][0] < 0 or d[i][0] >= n or d[i][1] < 0 or d[i][1] >= m:
      return cnt
    if board[d[i][0]][d[i][1]] != '*':
      return cnt
  
  for i in range(4):
    result[d[i][0]][d[i][1]] = '*'
  cnt += 1
  return cross(d, cnt)

ans = []
for i in range(n):
  for j in range(m):
    if board[i][j] == '*':
      direction = [[i, j] for _ in range(4)]
      cnt = cross(direction, 0)
      while cnt!=0:
        result[i][j] = '*'
        ans.append((i+1, j+1, cnt))
        cnt -= 1

if result == board:
  print(len(ans))
  for x, y , s in ans:
    print(x, y, s)
else:
  print(-1)