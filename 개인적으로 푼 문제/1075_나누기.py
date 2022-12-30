n=int(input())
f=int(input())
n=n-n%100
for i in range(100):
  if (n+i)%f==0:
    s=str(n+i)
    print(s[-2:])
    break