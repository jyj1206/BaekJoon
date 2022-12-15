import sys
input = sys.stdin.readline
n = int(input())
h = []
r = []
for i in range(n):
    x,y = map(int,input().split())
    h.append([x,y])
    r.append(1)

for i in range(n):
    for j in range(n):
        if h[i][0]<h[j][0] and h[i][1]<h[j][1]:
            r[i]+=1

for i in r:
    print(i,end=' ')