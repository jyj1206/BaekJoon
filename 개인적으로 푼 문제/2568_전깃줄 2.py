import sys
input = sys.stdin.readline

def lower_bound(start, end, num):
  while start <= end:
    mid = (start + end) //2
    if num <= d[mid]:
      end = mid - 1
    else:
      start = mid + 1       
  return start

n = int(input())
lines = []
for _ in range(n):
  a, b = map(int, input().split())
  lines.append((a, b))
lines.sort()

d = []
l = []

d.append(lines[0][1])
l.append(1)

for i in range(1, n):
  _, a = lines[i]
  if d[-1] < a:
    d.append(a)
    l.append(len(d))
  else:
    start = 0
    end = len(d) - 1
    idx = lower_bound(start, end, a)
    d[idx] = a
    l.append(idx + 1)

max_l = len(d)

print(n - max_l)

ans = []
remove = set()
for i in range(n-1, -1, -1):
  if max_l == l[i]:
    max_l -= 1
    remove.add(lines[i])
  if max_l == 0:
    break
  
for line in lines:
  if line not in remove:
    print(line[0])