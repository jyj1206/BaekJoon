from string import ascii_uppercase
n,b = map(int,input().split())
ans=''
nums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#nums=[str(i) for i in range(10)]+list(ascii_uppercase)
while(n!=0):
  #ans=nums[n%b]+ans
  ans+=str(nums[n%b])
  n//=b
print(ans[::-1])
#print(ans)

