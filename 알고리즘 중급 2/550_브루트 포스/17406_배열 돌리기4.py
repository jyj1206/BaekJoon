import sys
from itertools import permutations
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rotations = []

for _ in range(k):
  r, s, c = map(int, input().split())
  rotations.append((r, s, c))

def move(r, c, s, case):
  n = 2 * s
  temp = case[r - s][c + s]
  for i in range(n):
    case[r - s][c + s - i] = case[r - s][c + s - i - 1]
  for i in range(n):
    case[r - s + i][c - s] = case[r - s + i + 1][c - s]
  for i in range(n):
    case[r + s][c - s + i] = case[r + s][c - s + i + 1]
  for i in range(n):
    case[r + s - i][c + s] = case[r + s - i - 1][c + s]
  case[r - s + 1][c + s] = temp
  
def rotate(r, c, s, case):
  for i in range(1, s + 1):
    move(r, c, i, case)

INF = int(1e9)
result = INF
for order in permutations(rotations):
  case = [row[:] for row in board]
  for r, c, s in order:
    rotate(r - 1, c - 1, s, case)
  
  each_min = min(map(sum, case))
  result = min(result, each_min)

print(result)
