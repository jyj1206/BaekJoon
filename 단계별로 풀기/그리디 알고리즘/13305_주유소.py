import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split()))
p = list(map(int,input().split()))

ans=0
min_p=int(2e9)
for i in range(n-1):
  min_p=min(min_p,p[i])
  ans+=min_p*road[i]

print(ans)