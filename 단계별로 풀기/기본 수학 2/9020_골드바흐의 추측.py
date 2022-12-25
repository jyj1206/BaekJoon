import math
n=10000
num = [False,False]+[True]*(n-1)
for i in range(2,n+1):
    if num[i]:
        for j in range(i+i,n+1,i):
            if j%i==0:
                num[j]=False

t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(2,n//2+1):
        if num[i] and num[n-i]:
            a, b = i, n-i
    print(a, b)