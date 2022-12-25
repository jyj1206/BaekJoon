n, m = map(int,input().split())

ans=[]
def func(start):
    if len(ans)==m:
        print(" ".join(map(str,ans)))
        return

    for i in range(start,n+1):
        if i in ans:
            continue
        else:
            ans.append(i)
            func(i+1)
            ans.pop()      
func(1)