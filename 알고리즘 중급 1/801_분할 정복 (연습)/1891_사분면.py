import sys

def dq(n, idx, i, j):
  if n == 2:
    if cur[idx] == '1':
      return i, j+1
    elif cur[idx] == '2':
      return i, j
    elif cur[idx] == '3':
      return i+1, j
    else:
      return i+1, j+1
  
  half_n = n//2
  # 각 사분면
  if cur[idx] == '1':
    return dq(half_n , idx+1, i, j+half_n)
  elif cur[idx] == '2':
    return dq(half_n, idx+1, i , j)
  elif cur[idx]  == '3':
    return dq(half_n, idx+1, i + half_n, j)
  else:
    return dq(half_n, idx+1, i + half_n, j + half_n)

def loc(n, b_i, b_j, i, j, ans):
  if n == 1:
    return ans
  
  half_n = n//2
  if i< b_i + half_n and j < b_j + half_n:
    return loc(half_n, b_i, b_j, i, j, ans + '2')
  elif i < b_i + half_n and b_j + half_n <= j :
    return loc(half_n, b_i, b_j + half_n , i, j, ans + '1')
  elif b_i + half_n <= i and j < b_j + half_n :
    return loc(half_n, b_i + half_n, b_j, i, j, ans + '3')
  else : 
    return loc(half_n, b_i + half_n, b_j + half_n, i, j, ans + '4')  

input = sys.stdin.readline
d, cur = input().split()
x, y = map(int, input().split())
d = int(d)
s_n = 2**d

c_i, c_j = dq(s_n, 0, 0, 0)

n_i, n_j = c_i - y, c_j + x
if 0<= n_i< s_n and 0<= n_j < s_n:
  print(loc(s_n, 0, 0, n_i, n_j, ''))
else:
  print(-1)