import sys
input = sys.stdin.readline
while True:
  name, age, height = input().split()
  if name == '#':
    break
  print(name, 'Senior' if int(age) > 17 or int(height) >=80 else 'Junior')