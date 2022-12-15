t = int(input())

for i in range(t):
    H, W, N = map(int,input().split())
    w = 1+N//H
    h = N%H
    if(N%H==0): 
        w=N//H
        h=H
    print(f'{h*100+w}')