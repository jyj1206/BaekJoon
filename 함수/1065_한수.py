def func(num):
    a= list(map(int,str(num)))
    if len(a)==1: return True
    else:
        sub = a[1]-a[0]
        for i in range(len(a)-1):
            if sub!=a[i+1]-a[i] :
                return False
        return True
n=int(input())
count=0
for i in range(1,n+1):
    if func(i)==True:
        count+=1
print(count)