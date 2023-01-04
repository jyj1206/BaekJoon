n, b = input().split()

nums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans=0
for i in range(len(n)-1,-1,-1):
  ans+=pow(int(b),i)*nums.index(n[i])
print(ans)