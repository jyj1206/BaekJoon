import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
# +, -, *, %
oper = list(map(int,input().split()))
max_ans=-int(2e9)
min_ans=int(2e9)


def dfs(depth,add,sub,mul,div,ans):
  global max_ans, min_ans
  if depth==n:
    if max_ans<ans:
      max_ans=ans
    if min_ans>ans:
      min_ans=ans
    return
  
  if add:
    dfs(depth+1,add-1,sub,mul,div,ans+a[depth])
  
  if sub:
    dfs(depth+1,add,sub-1,mul,div,ans-a[depth])
  
  if mul:
    dfs(depth+1,add,sub,mul-1,div,ans*a[depth])
  
  if div:
    dfs(depth+1,add,sub,mul,div-1,int(ans/a[depth]))

dfs(1,oper[0],oper[1],oper[2],oper[3],a[0])

print(max_ans)
print(min_ans)
