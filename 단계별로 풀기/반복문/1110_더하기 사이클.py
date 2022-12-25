a = int(input())
x = a//10; y = a%10
sum=0
while(True):
    sum+=1
    z=x+y
    x=y; y=z%10
    if a==(x*10+y):
        break

print(sum)
