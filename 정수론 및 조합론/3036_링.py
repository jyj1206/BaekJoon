import sys
n = int(input())
num = list(map(int,input().split()))
def GCD(a,b):
    while b>0:
        a,b = b, a%b
    return a

for i in range(1,n):
    gcd=GCD(num[0],num[i])
    print(f"{num[0]/gcd:.0f}/{num[i]/gcd:.0f}")