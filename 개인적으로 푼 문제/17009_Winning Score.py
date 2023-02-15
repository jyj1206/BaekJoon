a3 = int(input()) * 3
a2 = int(input()) * 2
a1 = int(input()) 

b3 = int(input()) * 3
b2 = int(input()) * 2
b1 = int(input())

a = sum([a1, a2, a3])
b = sum([b1, b2, b3])

if a > b:
  print('A')
elif a < b:
  print('B')
else: 
  print('T')