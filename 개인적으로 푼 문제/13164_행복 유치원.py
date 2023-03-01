n, k = map(int, input().split())
h = list(map(int, input().split()))

dist = []
for i in range(1, n):
  dist.append(h[i] - h[i-1])
  
dist.sort()
print(sum(dist[:n-k]))