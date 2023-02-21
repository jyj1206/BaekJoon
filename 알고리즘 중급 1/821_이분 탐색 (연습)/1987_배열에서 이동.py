# pypy 3 통과
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
array = [list(map(int , input().split())) for _ in range(n)]

min_v = min(map(min, array))
max_v = max(map(max, array))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(diff):
  # s ~ e 범위의 값만 탐색 가능
  # 여기서 s가 될 수 있는 값은 min_v ~ max_v - diff 까지 가능
  # s 가 max_v -diff 보다 더 큰 값을 가질 때는 e 가 max_v의 값을 초과해 버림
  for s in range(min_v, max_v - diff + 1):
    e = s + diff
    
    # 시작 지점이 [s, e] 범위 안에 들어가지 않는 경우
    if array[0][0] < s or array[0][0] > e: 
      continue
    
    q = deque([(0,0)])
    visited = [[False for col in range(n)] for row in range(n)]
    visited[0][0] = True
    
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and s <= array[nx][ny] <= e:
          if (nx, ny)  == (n-1, n-1):
            return True
          visited[nx][ny] = True
          q.append((nx,ny))

  return False
  
low = 0
high = max_v - min_v
while low <= high:
  mid = (low + high)//2
  # 현재 (최대 - 최소) 값으로 dfs로 경로 도달이 가능한 경우 
  # (최대 - 최소) 값을 줄여줌
  if bfs(mid) :
    high = mid - 1
  else:
    low = mid + 1

print(low)