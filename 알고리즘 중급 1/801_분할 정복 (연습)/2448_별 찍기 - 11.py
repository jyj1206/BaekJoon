# 풀이 1 - 1줄씩 만들기
import sys
input = sys.stdin.readline
N = int(input())
def a(N):
    if N == 3:
        return ["  *  "," * * ","*****"]
    N //= 2
    x = a(N)
    A = [" " * N + i + " " * N for i in x]
    B = [i + " " + i for i in x]
    return A + B

print("\n".join(a(N)))

# 풀이 2 - 한점 기준 분할
# n = int(input())
# stars  = [[' ' for col in range(2 * n -1)] for row in range(n)]
# star = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]

# def dq(N, i, j):
#   if N == 3:
#     b_i = i
#     b_j = j-2
#     for x in range(3):
#       for y in range(5):
#         stars[b_i + x][b_j + y] = star[x][y]    
#     return    
  
#   dq(N//2, i, j)
#   dq(N//2, i + N//2, j - N//2)
#   dq(N//2, i + N//2, j + N//2)

# dq(n, 0, n - 1)

# for i in stars:
#   print("".join(i))