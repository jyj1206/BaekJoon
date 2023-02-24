import sys
input = sys.stdin.readline
graph = [list(input().split()) for _ in range(5)]

result = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(num, x, y):
  if len(num) == 6:
    result.add(int(num))
    return
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 5 and 0 <= ny < 5:
      dfs(num + graph[nx][ny], nx, ny)

for i in range(5):
  for j in range(5):
    dfs(graph[i][j], i, j)
    
print(len(result))