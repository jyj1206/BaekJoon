import sys
input = sys.stdin.readline
n = int(input())

cnt1=cnt2=0
def fib(n):
    global cnt1
    if n==1 or n==2:
        cnt1+=1
        return 1
    else : return fib(n-1)+fib(n-2)

def fibonacci(n):
    global cnt2
    f=[0,1,1]+[0]*(n-2)
    for i in range(3,n+1):
        cnt2+=1
        f[i]=f[i-1]+f[i-2]
    return f[n]

fib(n)
fibonacci(n)
print(cnt1,cnt2)
