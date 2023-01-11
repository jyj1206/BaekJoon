n= int(input())
i=1
ans=0
while(i<=n):
  ans+=n-i+1
  i*=10
print(ans)



# d=len(str(n))
# ans=0
# for i in range(d-1):
#   ans+=(9*pow(10,i))*(i+1)

# ans+=(n-pow(10,d-1)+1)*d

# print(ans)