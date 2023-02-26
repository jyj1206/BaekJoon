# 풀이 1 - dp
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 0 : 가로 1: 대각선 2 : 세로
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, n):
  if graph[0][i] != 1:
    dp[0][0][i] = dp[0][0][i-1]
  else:
    break

for i in range(1, n):
  for j in range(1, n):
    # 대각선 칸 처리
    if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
      dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

    if graph[i][j] == 0:
      dp[0][i][j] =  dp[0][i][j-1] + dp[1][i][j-1]
      dp[2][i][j] =  dp[1][i-1][j] + dp[2][i-1][j]

print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])

# 풀이 2 - dfs

# 풀이 3 bfs 시간 초과
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# move = [(0, 1), (1, 1), (1, 0)]


# def bfs():
#   result =0
#   # x, y, case, case : 0(가로), 1(대각선), 세로(2)
#   q = deque([(0, 1, 0)])
#   while q:
#     x, y, case = q.popleft()
    
#     for next in range(3):
#       if (case == 0 and next == 2) or (case == 2 and next == 0):
#         continue
#       nx = x + move[next][0]
#       ny = y + move[next][1]
      
#       if 0 <= nx < n and 0 <= ny < n :
#         if graph[nx][ny] == 1:
#           continue
#         if next == 1 and (graph[nx][ny - 1] == 1 or graph[nx - 1][ny] == 1):
#           continue
#         if (nx, ny) == (n-1, n-1):
#           result += 1
#           continue
#         q.append((nx, ny, next))

#   print(result)

# bfs()