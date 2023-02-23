import sys
input = sys.stdin.readline
lec = [list(input().split()) for _ in range(20)]

grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+': 2.5, 'C0' : 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

result = 0
total = 0
for _, g, r in lec:
  if r == 'P':
    continue
  total += float(g)
  result += float(g) * grade[r]

result = result / total

print(f"{result}")  