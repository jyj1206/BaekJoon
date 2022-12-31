li = [input()[0] for _ in range(int(input()))]
s =set(li)
ans=[]
for c in s:
  if li.count(c)>=5:
    ans.append(c)
print(''.join(sorted(ans)) if ans else 'PREDAJA')

# import sys
# input = sys.stdin.readline
# n = int(input())
# _dict={}
# for i in range(n):
#   s=input()[0]
#   if s in _dict:
#     _dict[s]+=1
#   else:
#     _dict[s]=1

# sorted_dict=sorted(_dict.items())
# flag=True
# for c in sorted_dict:
#   if c[1]>=5:
#     print(c[0], end='')
#     flag=False
# if flag:
#   print('PREDAJA')