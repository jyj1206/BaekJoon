import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))

visited=[0]*n
cnt=0

def dfs(i,sum):
  global cnt
  if i==n:
    return
  
  sum+=nums[i]
  if sum==s:
      cnt+=1
  
  dfs(i+1,sum)
  dfs(i+1,sum-nums[i])

dfs(0,0)
print(cnt)




# 비트쉬프트
# cnt = 0 # 조건에 맞는 경우 카운트
# for i in range(1 << n):
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(nums[j])
#     if sum(subset) == s:
#         cnt += 1
# if s == 0: # s가 0일경우 공집합을 포함하기때문에, 이 경우를 제외한다.
#     cnt -= 1
# print(cnt)

