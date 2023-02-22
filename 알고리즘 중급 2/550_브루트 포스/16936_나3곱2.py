import sys
input = sys.stdin.readline
n = int(input())
B = list(map(int, list(input().split())))
set_B = set(B)

def dfs(x, A):
  if len(A) == n:
    return A
  
  if x % 3 == 0:
    if x//3 in set_B:
      result = dfs(x//3, A + [x//3])
      if result:
        return result
      
  if x*2 in set_B:
    result = dfs(x * 2, A + [x * 2])
    if result:
      return result

for i in range(n):
  A = dfs(B[i], [B[i]])
  if A:
    print(*A)
    break