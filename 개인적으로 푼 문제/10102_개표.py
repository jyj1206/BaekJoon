n = int(input())
a = input().count('A')
b = n-a

if a>b:
  print('A')
elif a==b:
  print('Tie')
else:
  print('B')
#from collections import Counter
# n=int(input())
# vote=Counter(input())
# if vote['A']>vote['B']:
#   print('A')
# elif vote['A']<vote['B']:
#   print('B')
# else:
#   print('Tie')