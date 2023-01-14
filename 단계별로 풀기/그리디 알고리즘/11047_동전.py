import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins=[]
for i in range(n):
  coins.append(int(input()))

coins.reverse()
ans=0
for coin in coins:
  cnt=k//coin
  if cnt>0:
    ans+=cnt
    k-=cnt*coin

print(ans)