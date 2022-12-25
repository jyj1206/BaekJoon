# def func(num):
#     for i in range(2,num+1):
#         if num%i==0:
#             print(i)
#             func(num//i)
#             return

# num=int(input())
# func(num)

num=int(input())
i=2
while(num!=1):
    for i in range(i,num+1):
        if num%i==0:
            print(i)
            num//=i
            break