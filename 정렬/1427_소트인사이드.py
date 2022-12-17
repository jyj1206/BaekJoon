n = input()
num = list(map(int,str(n)))

num.sort(reverse=True)

for i in num:
    print(i,end='')
