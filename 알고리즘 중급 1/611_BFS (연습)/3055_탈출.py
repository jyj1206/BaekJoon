import sys
from collections import deque
input=sys.stdin.readline
r ,c = map(int,input().split())
forest=[list(input().strip()) for _ in range(r)]


dr=[1,0,-1,0]
dc=[0,1,0,-1]
def bfs():
  time=0
  sonic=deque()
  water=deque()
  visited=[[False for j in range(c)] for i in range(r)]
  for i in range(r):
    for j in range(c):
      if forest[i][j]=='*':
        water.append((i,j))
        visited[i][j]=True
      elif forest[i][j]=='S':
        sonic.append((i,j))
        visited[i][j]=True
      elif forest[i][j]=='X':
        visited[i][j]=True
        
  while sonic:
    time+=1
    for _ in range(len(water)):
      wi,wj = water.popleft()
      for i in range(4):
        nwi=wi+dr[i]
        nwj=wj+dc[i]
        if 0<=nwi<r and 0<=nwj<c and forest[nwi][nwj]=='.':
          water.append((nwi,nwj))
          forest[nwi][nwj]='*'
          visited[nwi][nwj]=True
    
    for _ in range(len(sonic)):
      si,sj=sonic.popleft()
      for i in range(4):
        nsi = si + dr[i]
        nsj = sj + dc[i]
        if 0<=nsi<r and 0<=nsj<c and not visited[nsi][nsj]:
          if forest[nsi][nsj]=='D':
            print(time)
            return
          sonic.append((nsi,nsj))
          visited[nsi][nsj]=True
          
  print("KAKTUS")
  
bfs()