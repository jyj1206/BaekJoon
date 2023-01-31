import sys
input =sys.stdin.readline
s = input().strip()
n=int(input())

prefix_sum={}
alpa=[0]*26
for i in range(len(s)):
  alpa[ord(s[i])-ord('a')]+=1
  prefix_sum[i]=alpa[:]

for i in range(n):
  q, l, r = input().split()
  l = int(l)
  r = int(r)
  idx = ord(q)-ord('a')
  if l==0:
    print(prefix_sum[r][idx])
  else:
    print(prefix_sum[r][idx]-prefix_sum[l-1][idx])