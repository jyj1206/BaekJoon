import sys
input =sys.stdin.readline
n = int(input())
p = list(map(int,input().split()))
p.sort()

sum=p[0]
for i in range(1,n):
  p[i]+=p[i-1]
  sum+=p[i]
print(sum)
