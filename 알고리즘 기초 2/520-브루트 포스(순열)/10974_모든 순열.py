from itertools import permutations
n = int(input())
nums=[i for i in range(1,n+1)]
for result in permutations(nums):
  print(*result)
  
# result=[]
# def permutation(depth):
#   if depth==n:
#     print(*result)
#     return

#   for i in range(1,n+1):
#     if i not in result:
#       result.append(i)
#       permutation(depth+1)
#       result.pop()

# permutation(0)