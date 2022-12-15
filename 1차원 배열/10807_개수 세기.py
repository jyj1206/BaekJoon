a = int(input())
N = list(map(int,input().split()))
v = int(input())
count=0
for i in range(len(N)):
    if N[i]==v : count+=1
print(count)