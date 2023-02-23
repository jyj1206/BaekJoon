import sys
input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input())
sticker = []

def check(r1, c1, r2, c2):
  if ((r1 + r2) <= h and max(c1, c2) <= w)  or ((c1 + c2) <= w and max(r1, r2) <= h):
    return True
  return False

for _ in range(n):
  r, c = map(int, input().split())
  sticker.append((r, c))

result = 0
for i in range(n):
  for j in range(i+1, n):
    r1, c1 = sticker[i]
    r2, c2 = sticker[j]
    
    if check(r1, c1, r2, c2):
      result = max(result, r1*c1 + r2*c2)
      continue
    # 두 스티커 모두 가로 세로가 같으면 둘다 회전 검증 x
    if r1 == c1 and r2 == c2:
      continue
    elif r1 == c1:
      if check(r1, c1, c2, r2):
        result = max(result, r1*c1 + r2*c2)
    elif r2 == c2:
      if check(c1, r1, r2, c2):
        result = max(result, r1*c1 + r2*c2)
    else:
      if check(r1, c1, c2, r2) or check(c1, r1, r2, c2) or check(c1, r1, c2, r2):
        result = max(result, r1*c1 + r2*c2)

print(result)