import sys
input = sys.stdin.readline

def lower_bound(start, end, target) :
  while start <= end :
    mid = (start + end) // 2
    if d[mid] >= target :
      end = mid - 1
    else:
      start = mid + 1
  return start

n = int(input())
a = list(map(int, input().split()))
d = []
ans = []
d.append(a[0])
ans.append(1)

for i in range(1, n):
  if d[-1] == a[i] :
    ans.append( len(d))
  elif d[-1] < a[i] :
    d.append(a[i])
    ans.append(len(d))
  else:
    start = 0
    end = len(d) - 1
    idx = lower_bound(start, end, a[i]);
    d[idx] = a[i]
    ans.append(idx + 1)

print(max(ans))