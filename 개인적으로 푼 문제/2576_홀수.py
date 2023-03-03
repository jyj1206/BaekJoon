odd = []
for _ in range(7):
  n = int(input())
  if n % 2 != 0:
    odd.append(n)

if len(odd) == 0:
  print(-1)
else:
  print(sum(odd))
  print(min(odd))