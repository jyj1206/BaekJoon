a=[[0 for i in range(100)] for j in range(100)]
count=0
n = int(input())
for k in range(n):
    r, c = map(int,input().split())
    for i in range(r,r+10):
        for j in range(c,c+10):
            a[i][j]=1

for row in a:
    count+=row.count(1)
print(count)