sum = int(input())
c = int(input())
sum2 = 0
for i in range(c):
    p, b = map(int,input().split())
    sum2+=p*b
print("Yes"if sum==sum2 else "No")