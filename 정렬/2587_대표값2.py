n=5
num=[]
for i in range(n):
    num.append(int(input()))
num.sort()
print(sum(num)//n)
print(num[n//2])