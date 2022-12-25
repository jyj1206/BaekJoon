n, m = map(int,input().split())

ans=[]
def func(i):
    #깊이가 최대 깊이랑 같아지면
    if i==m:
        print(" ".join(map(str,ans)))
        return

    for j in range(1,n+1):
        #ans에 이미 추가된 값이라면 continue
        if j in ans:
            continue
        else:
            ans.append(j)
            func(i+1)
            ans.pop()

func(0)