# combinations
from itertools import combinations
l,c =map(int,input().split())
vowel = {'a','e','i','o','u'}
s = input().split()
s.sort()

for ans in combinations(s,l):
  vow,con=0,0
  for c in ans:
    if c in vowel:
      vow+=1
    else:
      con+=1
  if vow>0 and con>1:
    print(''.join(ans))







# dfs 풀이
# def dfs(start,vow,con):
#   if vow>0 and con>1 and len(ans)==l:
#     print(''.join(ans))
#     return
  
#   for i in range(start,c):
#     if s[i] not in ans:
#       ans.append(s[i])
#       if s[i] in vowel:
#         dfs(i,vow+1,con)
#       else:
#         dfs(i,vow,con+1)
#       ans.pop()

# dfs(0,0,0)