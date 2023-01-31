import sys
input = sys.stdin.readline
n=int(input())
w = list(map(int,input().split()))
last = n-1

ans=0

# 구슬 삭제 한경우
def go(l,sum):
  global ans
  if l==1:
    ans=max(ans,sum)
    return
  for i in range(1,l):
    e = w[i-1]*w[i+1]
    temp=w.pop(i)
    go(l-1,sum+e)
    w.insert(i,temp)

go(last,0)
print(ans)

# 구슬 삭제 안하고 visited 사용
# visited=[0]*n
# def go(depth,sum):
#   global ans
#   if depth==n-2:
#     ans=max(ans,sum)
#     return
  
#   for i in range(start+1,last):
#     if not visited[i]:
#       visited[i]=1
#       left=i-1
#       right=i+1
#       while visited[left]:
#         left-=1
#       while visited[right]:
#         right+=1
#       go(depth+1,w[left]*w[right]+sum)
#       visited[i]=0

# go(0,0)
# print(ans)