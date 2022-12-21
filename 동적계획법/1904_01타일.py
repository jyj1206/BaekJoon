num = int(input())
def func(n):
    ans=[0,1,2]+[0]*(n-2)
    for i in range(3,n+1):
        ans[i]=ans[i-1]%15746+ans[i-2]%15746
    return ans[n]%15746

print(func(num))