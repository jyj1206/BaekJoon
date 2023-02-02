from collections import deque
dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

n = int(input())
visited=[[0 for j in range(n)] for i in range(n)] 

r1, c1, r2, c2 = map(int,input().split())

def bfs(s_i,s_j,e_i,e_j):
  queue = deque([(s_i,s_j)])
  visited[s_i][s_j]=1
  while queue:
    i, j = queue.popleft()
    if i == e_i and j == e_j:
      print(visited[e_i][e_j]-1)
      return 
    for k in range(6):
      ni = i+dr[k]
      nj = j+dc[k]
      if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
        visited[ni][nj]=visited[i][j]+1
        queue.append((ni,nj))
  print(-1)

bfs(r1,c1,r2,c2)