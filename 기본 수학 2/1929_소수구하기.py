a, b = map(int,input().split())

num=[False,False]+[True]*999999
for i in range(2,1000001):
    if num[i]:
        for j in range(i+i,1000001,i):
            num[j]=False

for i in range(a,b+1):
    if num[i]:
        print(i)