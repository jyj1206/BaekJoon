a, b = map(int,input().split())
m = int(input())
num = list(map(int,input().split()))

base_10=0
for i in range(m-1,-1,-1):
  base_10+=(a**(m-1-i))*num[i]

ans=[]
while(base_10!=0):
  ans.append(str(base_10%b))
  base_10//=b

ans.reverse()
print(' '.join(ans))