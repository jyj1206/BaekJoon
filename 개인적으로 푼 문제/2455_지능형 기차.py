result = 0
total = 0
for _ in range(4):
  a, b = map(int, input().split())
  total += b
  total -= a
  result = max(total, result)

print(result)