import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
  a.append((int(input()), i))
  
sorted_a = sorted(a)

ans = 0
for i in range(n):
  ans = max(ans,  sorted_a[i][1] - a[i][1])
  
print(ans + 1)