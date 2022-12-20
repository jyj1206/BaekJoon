import sys
input = sys.stdin.readline
n = int(input())
num=[]

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def divisor(a):
    div=[]
    for i in range(1,int(a**(1/2))+1):
        if a%i==0:
            div.append(i)
            if (i**2)!=a:
                div.append(a//i)
    div.sort()
    return div

for i in range(n):
    num.append(int(input()))

num_diff=[]
for i in range(n-1):
    num_diff.append(num[i+1]-num[i])

temp = num_diff[0]
for i in range(1, len(num_diff)):
    temp = gcd(num_diff[i],temp)

ans=divisor(temp)

for i in range(1,len(ans)):
    print(ans[i], end=' ')