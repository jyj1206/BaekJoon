import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
num=[]
for _ in range(n):
  num.append(int(input()))

cnt=Counter(num).most_common()

max_cnt = cnt[0][1]
ans = cnt[0][0]

for i in range(1,len(cnt)):
  if cnt[i][1]!=max_cnt:
    break
      
  ans=min(ans,cnt[i][0])

print(ans)