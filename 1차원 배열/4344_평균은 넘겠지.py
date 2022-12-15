c = int(input())
for i in range(c):
    a, *n = map(int,input().split())
    avr=sum(n)/a
    count=0
    for i in range(a):
        if n[i]<=avr:
            count+=1
    print(f'{(a-count)/a*100:.3f}%')