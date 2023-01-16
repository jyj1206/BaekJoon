from itertools import combinations
n=[int(input()) for i in range(9)]
for combi in combinations(n,7):
  if sum(combi)==100:
    for i in sorted(combi):
      print(i)
    break


# n.sort()
# sumh=sum(n)
# for i in range(9):
#   for j in range(9):
#     if i!=j:
#       if sumh-n[i]-n[j]==100:
#         find=(i,j)

# for i in range(9):
#   if i not in find:
#     print(n[i])