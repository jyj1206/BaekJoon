import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
target = int(input())

# 정렬 + 투 포인터
a.sort()
ans=0
l=0
r=n-1
while l<r:
  if target>a[l]+a[r]:
    l+=1
  elif target<a[l]+a[r]:
    r-=1
  else:
    ans+=1
    l+=1
    r-=1

print(ans)

# 딕셔너리
# _dict={}
# ans=0
# for i in range(n):
#   if target-a[i] in _dict:
#     ans+=1
#   _dict[a[i]]=1

# print(ans)