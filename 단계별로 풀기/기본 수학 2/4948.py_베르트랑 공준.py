n=123456
num = [False,False]+[True]*(2*n-1)
for i in range(2,2*n+1):
    if num[i]:
        for j in range(i+i,n*2+1,i):
            if j%i==0:
                num[j]=False

t=int(input())
while(t!=0):
    count=0
    for i in range(t+1,t*2+1):
        if num[i]:
            count+=1
    print(count)
    t=int(input())
