import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
  a, b = input().split()
  b = int(b)
  
  if b >= 90:
    grade = 'A'
  elif b >= 80:
    grade = 'B'
  elif b >= 70:
    grade = 'C'
  elif b >= 60:
    grade = 'D'
  else:
    grade = 'F'
    
  if grade != 'F' :
    if b % 10 > 6 or b == 100:
      grade += '+'
  
  print(a, grade)