n, p = map(int, input().split())
num = [0] * 97
cur = n
count = 1

while True:
  next = (cur * n) % p
  if num[next]:
    print(count - num[next] + 1)
    break
  count += 1  
  num[next] = count
  cur = next