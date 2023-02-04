import sys
from collections import deque
input = sys.stdin.readline

def mode(m,v):
  if m==0:
    v=(v*2)%10000
  elif m==1:
    v=(v-1)%10000
  elif m==2:
    v=(v%1000)*10+v//1000
  else:
    v=(v%10)*1000+v//10
  return v

def bfs(a,b):
  q=deque([(a,'')])  
  visited=[0]*10000
  visited[a]=1
  oper = ['D','S','L','R']
  while q:
    cur_v ,opers =q.popleft()
    for i in range(4):
      next_v= mode(i,cur_v)
      if not visited[next_v]:
        if next_v==b:
          return opers+oper[i]
        visited[next_v]=1
        q.append((next_v,opers+oper[i]))

t = int(input())
for i in range(t):
  a,b = map(int,input().split())
  print(bfs(a,b))