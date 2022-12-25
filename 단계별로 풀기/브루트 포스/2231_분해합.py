n = int(input())
i=1
while(n>i):
    a=list(map(int,str(i)))
    x=sum(a)
    if x+i==n:
        break
    i+=1
if n==i :
    print(0)
else:
    print(i)