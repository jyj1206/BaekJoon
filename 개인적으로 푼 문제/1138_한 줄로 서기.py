n = int(input())
s = list(map(int,input().split()))
ans=[0]*n

#풀이 1
for i in range(n):
  cnt=0
  for j in range(n):
    if cnt == s[i] and ans[j]==0:
      ans[j]=i+1
      break
    if ans[j]==0:
      cnt+=1
      
print(*ans)








#ans=[]
# 풀이2
# s= s[::-1]
# for i in s:
#   ans.insert(i,n)
#   n-=1
# print(*ans)

# 내 풀이
# n = int(input())
# s = list(map(int,input().split()))
# ans=[]
# for i in range(n-1,-1,-1):
#   t=s[i]
#   idx=0
#   while t!=0:
#     if ans[idx]>i:
#       t-=1
#     idx+=1
#   ans.insert(idx,i+1)
# print(*ans)