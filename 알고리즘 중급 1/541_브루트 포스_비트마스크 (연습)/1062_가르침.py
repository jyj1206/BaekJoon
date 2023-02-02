import sys
from itertools import combinations
input = sys.stdin.readline
n, k = map(int,input().split())
must = set(['a','n','t','i','c'])
candidates = set()
words=[]
for i in range(n):
  w = list(input().strip())
  temp=0
  for c in w:
    temp|=1<<(ord(c)-ord('a'))
    candidates.add(c)
  words.append(temp)

# antic 표현 불가
if k<5:
  print(0)
# 익힌 글자로 모든 단어를 충분히 표현 가능한 경우
elif k==26 or len(candidates)<=k:
  print(n)
else:
  candidates = candidates - must
  ans=0
  for i in combinations(candidates,k-5):
    temp=0
    cnt=0
    # 반드시 포함 되어야 하는 알파벳
    for alpa in must:
      temp|=1<<(ord(alpa)-ord('a'))
    
    for alpa in i:
      temp|=1<<(ord(alpa)-ord('a'))
    
    for word in words:
      if (word&temp) == word:
        cnt+=1
    
    ans=max(ans,cnt)
    
  print(ans)

# # a,n,t,i,c
#import sys
# import string
# from itertools import combinations
# input = sys.stdin.readline
# n, k = map(int,input().split())
# words = [input().strip() for i in range(n)]
# must= set(['a','n''t','i','c'])
# if k<5:
#   print(0)
# else:
#   must = set(['a','n','t','i','c'])
#   alpa = set([i for i in string.ascii_lowercase])
#   comb_alpa = alpa-must
#   alpa_words=[]
#   ans=0
#   for word in words:
#     temp=0
#     for c in word:
#       temp|=1<<(ord(c)-ord('a'))
#     alpa_words.append(temp)
  
#   for i in combinations(comb_alpa,k-5):
#     temp=0
#     cnt=0
#     for a in i:
#       temp|=1<<(ord(a)-ord('a'))
    
#     for a in must:
#       temp|=1<<(ord(a)-ord('a'))

#     for alpa_word in alpa_words:
#       if (alpa_word&temp)==alpa_word:
#         cnt+=1
    
#     ans=max(ans,cnt)
    
#   print(ans)