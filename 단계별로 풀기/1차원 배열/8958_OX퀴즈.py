a=int(input())
for i in range(a):
    sum=0
    count=0
    test_case = list(input())
    for i in range(len(test_case)):
        if test_case[i]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)

