import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
board=[]
for i in range(n):
  board.append(list(input().strip()))

coin=[]
for i in range(n):
  for j in range(m):
    if board[i][j]=='o':
      coin.append((i,j))

a = coin[0]
b = coin[1]

dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 동전이 떨어졌는지 확인
def check(i,j):
  if 0<=i<n and 0<=j<m:
    return False
  return True

def bfs(a,b):
  queue = deque([[a,b,0]])
  visited.add((a[0],a[1],b[0],b[1]))
  while queue:
    cur_a, cur_b, depth =queue.popleft()
    if depth==10:
      return -1
    if cur_a==cur_b:
      continue
    for i in range(4):
      a_i = cur_a[0]+dr[i]
      a_j = cur_a[1]+dc[i]
      b_i = cur_b[0]+dr[i]
      b_j = cur_b[1]+dc[i]
      # a,b 둘다 떨어지면
      if check(a_i,a_j) and check(b_i,b_j):
        continue
      # a만 떨어지면
      elif check(a_i,a_j):
        return depth+1
      # b만 떨어지면
      elif check(b_i,b_j):
        return depth+1
      # a,b 둘다 안 떨어지면
      else:
        # a가 벽으로 가면, 가기 전 위치로
        if board[a_i][a_j]=='#':
          a_i,a_j= cur_a[0],cur_a[1]
        # b가 벽으로 가면, 가기 전 위치로
        if board[b_i][b_j]=='#':
          b_i,b_j = cur_b[0],cur_b[1]
        # 두 동전이 있었던 위치가 아니면
        if (a_i,a_j,b_i,b_j) not in visited:
          queue.append([(a_i,a_j),(b_i,b_j),depth+1])
          visited.add((a_i,a_j,b_i,b_j))
  return -1

visited=set()
ans=bfs(coin[0],coin[1])

print(ans)