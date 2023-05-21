num = list(map(int, input()))
def part(ary):
  mul = 1
  for i in ary:
    mul *= i
  return mul

if len(num) == 1:
  print('NO')
else:
  flag = False
  for i in range(1, len(num)):
    if part(num[:i]) == part(num[i:]):
      flag = True
      break
  print('YES' if flag else 'NO')