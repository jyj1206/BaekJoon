import sys
input = sys.stdin.readline

def lower_bound(start, end, target):
  while start <= end:
    mid = (start + end)//2
    
    if d[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
  return start

n = int(input())
a = list(map(int, input().split()))

d = [a[0]]
l = [1]

for i in range(1, n):
  if d[-1] < a[i]:
    d.append(a[i])
    l.append(len(d))
  elif d[-1] == a[i]:
    l.append(len(d))
  else:
    idx = lower_bound(0, len(d) - 1, a[i])
    d[idx] = a[i]
    l.append(idx + 1)

print(n - max(l))