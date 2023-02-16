x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

if r1+r2 <= d:
  print("NO")
else:
  print("YES")