import sys
a = sys.stdin.read().replace(' ','').replace('\n','')
alpa = [0]*26
for c in a:
  if c.islower():
    alpa[ord(c)-ord('a')]+=1

for i in range(26):
  if alpa[i]==max(alpa):
    print(chr(i+ord('a')),end='')

# from collections import Counter
# cnt=Counter(a).most_common()
# cnt.sort(key=lambda x:(-x[1],x[0]))

# for i in range(len(cnt)):
#   if cnt[0][1]==cnt[i][1]:
#     print(cnt[i][0],end='')
#   else:
#     break