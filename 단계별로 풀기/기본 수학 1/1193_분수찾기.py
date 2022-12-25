n=int(input())

max_num=0
line=0
while(n>max_num):
    line+=1
    max_num+=line

index=n-max_num+line

if line%2==0:
    print(f'{index}/{line+1-index}')
else:
    print(f'{line+1-index}/{index}')