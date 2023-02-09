import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited = [[k+1 for _ in range(m)] for _ in range(n)]
  visited[0][0] = 0
  time = 1
  while q:
    # 낮 1, 밤 0
    day = time % 2
    for _ in range(len(q)):
      x, y, d = q.popleft()
      if (x, y) == (n-1, m-1):
        print(time)
        return
      for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < n and 0 <= ny < m:
          # 현재까지 부순 벽의 개수
          # 덜 부서서 도착할 수 있는 경우, 낮과 밤 관계 없음
          if not board[nx][ny] and d < visited[nx][ny]:
            visited[nx][ny] = d
            q.append((nx, ny, d))  
          
          if board[nx][ny] and d + 1 < visited[nx][ny]:
            if day == 0 :
              q.append((x, y, d))
            else:
              visited[nx][ny] = d + 1
              q.append((nx, ny, d + 1))
    time += 1
  print(-1)

bfs()