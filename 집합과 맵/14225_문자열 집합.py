import sys
input=sys.stdin.readline
n,m=map(int,input().split())
N=[]
M=[]
for i in range(n):
    N.append(input().strip())
for m in range(m):
    M.append(input().strip())

_dict={}
for word in N:
    _dict[word]=0

count=0
for word in M:
    if word in _dict:
        count+=1

print(count)