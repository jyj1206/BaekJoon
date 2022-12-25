start=int(input())
end=int(input())
sosu=[]

for num in range(start,end+1):
    if num>1:
        prime=True
        for i in range(2,num):
            if(num%i==0):
                prime=False
        if prime==True:
            sosu.append(num)
if sosu:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
