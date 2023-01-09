a=int(input())
b=int(input())
c=int(input())
s=list(str(a*b*c))
for i in range(10):
  print(s.count(str(i)))