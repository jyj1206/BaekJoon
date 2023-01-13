n = int(input())
cute=0
for i in range(n):
  if int(input())==1:
    cute+=1

print("Junhee is cute!" if cute>n-cute else "Junhee is not cute!")