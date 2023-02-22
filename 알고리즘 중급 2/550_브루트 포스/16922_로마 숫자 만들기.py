# 풀이 1
from itertools import combinations_with_replacement

n = int(input())
iterator = [1, 5, 10, 50]
ans = set()

for i in combinations_with_replacement(iterator, n):
  ans.add(sum(i))

print(len(ans))

# 풀이 2
# N = int(input())
# s = set()
# for i in range(N+1):
#     for j in range(N+1 - i):
#         for k in range(N+1 - i - j):
#             t = N-i-j-k
#             n = i + 5*j + 10*k  + 50*t
#             s.add(n)

# print(len(s))

# 풀이 3
# n = int(input())

# number = ['I', 'V', 'X', 'L']
# visited = set()
# case = []
# def dfs(I, V, X, L, depth):
#   if (I, V, X, L) in visited:
#     return
#   visited.add((I, V, X, L))
#   if depth == n:
#     total = I + V * 5 + X * 10 + L * 50
#     if total not in case:
#       case.append(total) 
#     return
  
#   for num in number:
#     if num == 'I':
#       dfs(I + 1, V, X, L, depth + 1)
#     elif num == 'V':
#       dfs(I, V + 1, X, L, depth + 1)
#     elif num == 'L':
#       dfs(I, V , X + 1 ,L, depth + 1)
#     else:
#       dfs(I, V , X  ,L + 1, depth + 1)

# dfs(0, 0, 0, 0, 0)
# print(len(case))