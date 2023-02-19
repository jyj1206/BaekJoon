n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
  mid = (start + end) // 2
  
  total = 0
  for i in range(1, n + 1):
    cnt = mid // i
    total += min(cnt, n)
  
  if total >= k:
    end = mid - 1
  else:
    start = mid + 1

print(start) 