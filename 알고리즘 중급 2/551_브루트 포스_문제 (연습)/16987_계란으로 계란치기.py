import sys
input = sys.stdin.readline
n = int(input())
egg = []

for _ in range(n):
  s, w = map(int, input().split())
  egg.append([s, w])

breaked = [False] * n

result = 0

def dfs(idx, breaked_n):
  global result
  if idx == n:
    result = max(result, breaked_n)
    return
  
  if breaked[idx]:
    dfs(idx + 1, breaked_n)
    return
  
  flag = True
  for i in range(n):
    if i == idx or breaked[i]:
      continue
    cnt = 0
    
    flag = False
    
    egg[idx][0] -= egg[i][1]
    egg[i][0] -= egg[idx][1]
    
    if egg[idx][0] <= 0:
      cnt += 1
      breaked[idx] = True
      
    if egg[i][0] <= 0:
      cnt += 1
      breaked[i] = True
    
    dfs(idx + 1, breaked_n + cnt)
    
    egg[idx][0] += egg[i][1]
    egg[i][0] += egg[idx][1]
    
    breaked[i] = False
    breaked[idx] = False
  if flag :
    result = max(result, breaked_n)
    return
  
dfs(0, 0)
print(result)
  
    