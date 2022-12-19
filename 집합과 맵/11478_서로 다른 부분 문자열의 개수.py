n=input()
set=set()
for i in range(len(n)):
    for j in range(i,len(n)):
        print(i,j, end=' ')
        set.add(n[i:j+1])
print(len(set))