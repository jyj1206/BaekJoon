import sys
input = sys.stdin.readline

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

n = int(input())
to_port = list(map(int, input().split()))

d = [to_port[0]]
l = [1]

for i in range(1, n):
  if d[-1] < to_port[i]:
    d.append(to_port[i])
    l.append(len(d))
  elif d[-1] == to_port[i]:
    l.append(len(d))
  else:
    idx = lower_bound(to_port[i])
    d[idx] = to_port[i]
    l.append(idx + 1)

print(len(d))