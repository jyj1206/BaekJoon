# 풀이 1
import sys
input = sys.stdin.readline
target = input().strip()
n = int(input())

cnt = 0
for _ in range(n):
  ring = input().strip()
  
  if target in ring*2:
    cnt += 1

print(cnt)

# 풀이 2
# import sys
# def solution() :
#   for i in range(10):
#     for j in range(len(target)):
#       if ring[(i+j)%10] != target[j]:
#         break
#     else:
#       return True
#   return False

# input = sys.stdin.readline
# target = input().strip()
# n = int(input())

# count = 0
# for _ in range(n):
#   ring = input().strip()
#   if solution():
#     count += 1

# print(count)