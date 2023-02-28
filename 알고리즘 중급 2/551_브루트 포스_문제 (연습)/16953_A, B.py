a, b = map(int, input().split())

def dfs(num, cnt):
  if num < a:
    return -1
  elif num == a:
    return cnt + 1
  else:
    if num % 10 == 1:
      return dfs(num//10, cnt + 1)
    elif num % 2 == 0:
      return dfs(num//2, cnt + 1)
    return -1

print(dfs(b, 0))
