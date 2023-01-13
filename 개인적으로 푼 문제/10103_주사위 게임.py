n = int(input())
s1,s2=100,100
for i in range(n):
  a,b=map(int,input().split())
  if a>b:
    s2-=a
  elif a<b:
    s1-=b
print(s1)
print(s2)