n, m = map(int,input().split())

ans=[]
def func(depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return

    for i in range(1,n+1):
        ans.append(i)
        func(depth+1)
        ans.pop()

func(0)