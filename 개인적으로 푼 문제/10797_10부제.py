n = int(input())
c = list(map(int,input().split()))

cnt=0
for i in c:
  if i==n:
    cnt+=1
print(cnt)