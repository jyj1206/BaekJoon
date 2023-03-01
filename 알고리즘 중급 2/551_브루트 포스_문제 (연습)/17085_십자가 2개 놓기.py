import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

def find_cross(x, y):
  cross_size = 0
  while True:
    cnt = cross_size + 1
    if 0 > x - cnt or x + cnt >= n or 0 > y - cnt or y + cnt >= m: 
      break
    if board[x - cnt][y] == '.' or board[x + cnt][y] == '.' or board[x][y - cnt] == '.' or board[x][y + cnt] == '.':
      break
    cross_size += 1
  return cross_size

def area(size):
  return 4*size + 1

cross = []
for i in range(n):
  for j in range(m):
    if board[i][j] == '#':
      cross_size = find_cross(i, j)
      cross.append((i, j, cross_size))
      
def check(x2, y2, cur_size2):
  if visited[x2][y2]:
    return False
  for size in range(1, cur_size2 + 1):
    if visited[x2 - size][y2] or visited[x2 + size][y2] or visited[x2][y2 - size] or visited[x2][y2 + size]:
      return size - 1
  if cur_size2 == 0:
    return 0
  return size

result  = 1
for i in range(len(cross) - 1):
  for j in range(i + 1, len(cross)):
    x1, y1, size1 = cross[i]
    x2, y2, size2 = cross[j]
    
    max_size1 = size1
    max_size2 = size2
    
    if area(max_size1) * area(max_size2) > result:
      visited = [[False] * m for _ in range(n)]
      visited[x1][y1] = True
      
      for size in range(1, max_size1 + 1):
        visited[x1 - size][y1] = True
        visited[x1 + size][y1] = True
        visited[x1][y1 - size] = True
        visited[x1][y1 + size] = True
      
      while area(max_size1) * area(max_size2) > result:
        valid_size = check(x2, y2, max_size2)
        
        if valid_size:
          result =  max(result, area(max_size1) * area(valid_size))

        visited[x1 - max_size1][y1] = False
        visited[x1 + max_size1][y1] = False
        visited[x1][y1 - max_size1] = False
        visited[x1][y1 + max_size1] = False
        max_size1 -= 1
        
print(result)
    