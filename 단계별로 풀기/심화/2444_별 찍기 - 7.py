n = int(input())
star = '*'
stars = []
for i in range(1, n + 1):
  stars.append(' ' * (n-i) + star * (2 * i - 1))

for i in range(1, n):
  stars.append(' ' * i + star * (2 * (n - i) - 1))

for i in stars:
  print(i)