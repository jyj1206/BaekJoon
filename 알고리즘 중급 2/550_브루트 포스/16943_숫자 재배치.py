from itertools import permutations
a, b = input().split()
a_digit = len(a)
b_digit = len(b)

if a_digit > b_digit:
  print(-1)
else:
  a = sorted(list(a))
  b = int(b)
  c = -1 
  for perm in permutations(a):
    if perm[0] == '0':
      continue
    n = int("".join(perm))
    if n < b:
      c = max(c, n)
    else:
      break
  
  print(c)