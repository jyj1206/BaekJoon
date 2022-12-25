a=int(input())
number=map(int,input().split())
sosu=0
for num in number:
    if num>1:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
        if prime==True:
            sosu+=1
print(sosu)