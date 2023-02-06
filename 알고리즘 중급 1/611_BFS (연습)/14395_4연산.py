from collections import deque
s, t = map(int,input().split())
visited=set()

def check(n):
  if 0<=n<=10**9:
    return True
  else:
    return False

def bfs(s,t):
  q = deque()
  # 초기값 설정
  visited.add(s)
  for o in "*+-/":
    if o=='*':
      next_n=s*s
    elif o =='+':
      next_n=s+s
    elif o =='-':
      next_n=0
    else:
      if s==0:
        continue
      next_n=1

    if check(next_n) and next_n not in visited:
      visited.add(next_n)
      q.append((next_n,o))

  while q:
    n, oper =q.popleft()
    
    if n==t:
      print(oper)
      return
    
    next_n = n*n
    if check(next_n) and next_n not in visited:
      visited.add(next_n)
      q.append((next_n,oper+'*'))
    
    next_n = n+n
    if check(next_n) and next_n not in visited:
      visited.add(next_n)
      q.append((next_n,oper+'+'))
      
  print(-1)
  
  
if s==t:
  print(0)
else:
  bfs(s,t)