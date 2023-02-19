x, y, c = map(float , input().split())

def cal_c(w):
  h1 = (x**2 - w**2) ** 0.5
  h2 = (y**2 - w**2) ** 0.5
  return (h1*h2) / (h1 + h2)
  


low = 0
high = min(x, y)

while (high - low) >= 0.000001:
  w = (low + high) / 2
  
  if cal_c(w) >= c:
    low = w
  else:
    high = w

print(f"{low:.3f}")