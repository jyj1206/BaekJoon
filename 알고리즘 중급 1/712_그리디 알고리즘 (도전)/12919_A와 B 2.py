import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()
diff = len(t) - len(s)

# dfs 풀이
def dfs(t, depth):
  if t == s:
    print(1)
    sys.exit()
  
  if depth == diff:
    return
  
  if t[0] == 'B':
    dfs(t[::-1][:-1], depth + 1)
  
  if t[-1] == 'A':
    dfs(t[:-1], depth +1)

dfs(t, 0)
print(0)

# bfs 풀이
# import sys
# from collections import deque
# input = sys.stdin.readline
# s = input().strip()
# t = input().strip()
# def bfs():
#   diff = len(t) -len(s)
#   q = deque([t])
#   while q and diff!=0:
#     visited = set()
#     for _ in range(len(q)):
#       c_t = q.popleft()
#       if c_t[-1] == 'A':
#         n_t = c_t[:-1]
#         if n_t not in visited:
#           q.append(n_t)
#           visited.add(n_t)
      
#       if c_t[0] == 'B':
#         n_t = c_t[::-1][:-1]
#         if n_t not in visited:
#           q.append(n_t)
#           visited.add(n_t)
#     diff-=1
#   return q

# result = bfs()
# if s in result:
#   print(1)
# else:
#   print(0)