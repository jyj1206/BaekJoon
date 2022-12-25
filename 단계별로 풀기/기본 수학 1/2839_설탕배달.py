def func(s,max_count_5):
    for count5 in reversed(range(max_count_5+1)):
        temp=s
        temp-=count5*5
        if(temp%3==0):
            count_3=temp//3
            return(count_3+count5)
    return -1

sugar=int(input())
print(func(sugar,sugar//5))