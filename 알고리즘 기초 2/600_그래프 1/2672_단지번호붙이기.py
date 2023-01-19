import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
table=[list(map(int,input().strip()))for i in range(n)]
# 위,오른쪽,아래,왼쪽
dr = [-1,0,1,0]
dc = [0,1,0,-1]

cnt=0
def dfs(i,j):
  global cnt
  table[i][j]=0
  cnt+=1
  
  for k in range(4):
    ni=i+dr[k]
    nj=j+dc[k]
    if  0<=ni<n and 0<=nj<n and table[ni][nj]!=0:
      dfs(ni,nj)
      
  # if -1<i+dr[0] and table[i+dr[0]][j+dc[0]]!=0:
  #   dfs(i+dr[0],j+dc[0])
    
  # if j+dc[1]<n and table[i+dr[1]][j+dc[1]]!=0:
  #   dfs(i+dr[1],j+dc[1])
    
  # if i+dr[2]<n and table[i+dr[2]][j+dc[2]]!=0:
  #   dfs(i+dr[2],j+dc[2])
    
  # if -1<j+dc[3] and table[i+dr[3]][j+dc[3]]!=0:
  #   dfs(i+dr[3],j+dc[3])

home_num=0
homes=[]
for i in range(n):
  for j in range(n):
    if table[i][j]!=0 :
      home_num+=1
      dfs(i,j)
      homes.append(cnt)
      cnt=0
      
print(home_num)
for home in sorted(homes):
  print(home)