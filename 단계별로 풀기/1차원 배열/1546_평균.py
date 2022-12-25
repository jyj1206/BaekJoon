a=int(input())
n=list(map(int,input().split()))

new_list=[]
for i in range(a):
    new_list.append(n[i]/max(n))

print(sum(new_list)/a*100)

