import sys

def lower_bound(target):
  start = 0
  end = len(d) - 1
  while start <= end:
    mid = (start + end) // 2
    
    if d[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
  return start

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

d = [a[0]]
l = [1]

for i in range(1, n):
  if a[i] > d[-1]:
    d.append(a[i])
    l.append(len(d))
  elif a[i] == d[-1]:
    l.append(len(d))
  else:
    idx = lower_bound(a[i])
    d[idx] = a[i]
    l.append(idx + 1)

max_l = len(d)
print(max_l)