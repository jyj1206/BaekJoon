import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
s_list=[]
b_list=[]
for i in range(n):
  s, b = map(int,input().split())
  s_list.append(s)
  b_list.append(b)

ans=abs(s_list[0]-b_list[0])

def dfs(i,s_sum,b_sum):
  global ans
  if i==n:
    if s_sum==1 and b_sum==0:
      return
    ans=min(ans,abs(s_sum-b_sum))
    return

  dfs(i+1,s_sum,b_sum)
  dfs(i+1,s_sum*s_list[i],b_sum+b_list[i])

dfs(0,1,0)

print(ans)

# 비트마스크
# for i in range(1,1<<n):
#   s_sum=1
#   b_sum=0
#   for j in range(n):
#     if i&(1<<j):
#       s_sum*=s_list[j]
#       b_sum+=b_list[j]
#   ans=min(ans,abs(s_sum-b_sum))
  
# print(ans)