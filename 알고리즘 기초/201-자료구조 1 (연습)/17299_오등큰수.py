from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int,input().split()))
result = [-1]*n

freq=Counter(seq)
# freq={}
# for i in range(n):
#   if seq[i] in freq:
#     freq[seq[i]]+=1
#   else:
#     freq[seq[i]]=1

stack=[]
for i in range(n):
  while stack and freq[seq[i]]>freq[seq[stack[-1]]]:
    top=stack.pop()
    result[top]=seq[i]
  stack.append(i)

print(' '.join(map(str,result)))