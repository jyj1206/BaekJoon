import sys
input = sys.stdin.readline
c, p = map(int, input().split())
h = list(map(int, input().split()))

result = 0

def check_4(d1, d2, d3, d4):
  cnt = 0
  for i in range(c - 3):
    if h[i] - d1 == h[i + 1] - d2 and h[i + 1] - d2 == h[i + 2] - d3 and h[i + 2] - d3 == h[i + 3] - d4:
      cnt += 1
  return cnt

def check_3(d1, d2, d3):
  cnt = 0
  for i in range(c - 2):
    if h[i] - d1 == h[i + 1] - d2 and h[i + 1] - d2 == h[i + 2] - d3:
      cnt += 1
  return cnt
      
def check_2(d1, d2):
  cnt = 0
  for i in range(c - 1):
    if h[i] - d1 == h[i + 1] - d2:
      cnt += 1
  return cnt
      
if p == 1:
  result += check_4(0, 0, 0, 0) + c
elif p == 2:
  result += check_2(0, 0)
elif p == 3:
  result += check_3(0, 0, 1) + check_2(1, 0)
elif p == 4:
  result += check_3(1, 0, 0) + check_2(0, 1)
elif p == 5:
  result += check_3(0, 0, 0) + check_2(0, 1) + check_2(1, 0) + check_3(1, 0, 1)
elif p == 6:
  result += check_3(0, 0, 0) + check_2(0, 0) + check_2(2, 0) + check_3(0, 1, 1)
else:
  result += check_3(0, 0, 0) + check_2(0, 0) + check_2(0, 2) + check_3(1, 1, 0)

print(result)