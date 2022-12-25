import sys
input = sys.stdin.readline
n= int(input())
s = list(map(int,input().split()))
left = [0]*n
right = [0]*n

for i in range(0,n):
    for j in range(i):
        if s[i]>s[j]:
            left[i]=max(left[i],left[j]+1)

    for j in range(n-1,n-i-1,-1):
        if s[n-i-1]>s[j]:
            right[n-i-1]=max(right[n-i-1],right[j]+1)

dp=[]
for i in range(n):
    dp.append(left[i]+right[i]+1)

print(max(dp))