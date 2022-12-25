T = int(input())
count=0
for i in range(T):
    count+=1
    n = input()
    s = set(n)
    for alpa in s:
        temp = alpa*n.count(alpa)
        if n.find(temp)==-1:
            count-=1
            break
print(count)