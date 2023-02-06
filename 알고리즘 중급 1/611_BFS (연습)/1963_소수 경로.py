import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

# 에라토스테네스의 체
max_value=9999
is_prime =[False, False]+[True]*(max_value-1)
for i in range(2,int(max_value**0.5)+1):
  if is_prime[i]:
    for j in range(i,max_value+1,i+i):
      is_prime[j]=False

def bfs(a,b):
  visited=set()
  visited.add(a)
  q = deque([(a,0)])
  while q:
    cur_n,cost=q.popleft()
    if cur_n==b:
      print(cost)
      return
    for i in range(4):
      temp=cur_n-cur_n%(10**(i+1))+cur_n%(10**i)
      for j in range(10):
        if i==3 and j==0:
          continue
        next_n= temp + j*(10**i)
        if is_prime[next_n] and next_n not in visited:
          visited.add(next_n)
          q.append((next_n,cost+1))
  print('Impossible')

for i in range(t):
  a, b = map(int,input().split())
  bfs(a,b)