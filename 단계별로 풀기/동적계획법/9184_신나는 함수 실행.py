import sys
input = sys.stdin.readline

def func():
    w=[[[0 for i in range(21)]for j in range(21)]for k in range(21)]
    for a in range(21):
        for b in range(21):
            for c in range(21):
                if a<=0 or b<=0 or c<=0: w[a][b][c]=1
                elif a<b and b<c : 
                    w[a][b][c]=w[a][b][c-1]+w[a][b-1][c-1]-w[a][b-1][c]
                else: 
                    w[a][b][c]=w[a-1][b][c]+w[a-1][b-1][c]+w[a-1][b][c-1]-w[a-1][b-1][c-1]
    return w
        
ans=func()
while (True):
    a, b, c =map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        value=ans[0][0][0]
    elif a>20 or b>20 or c>20:
        value=ans[20][20][20]
    else:
        value=ans[a][b][c]
    print(f'w({a}, {b}, {c}) = {value}')
    