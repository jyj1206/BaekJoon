s=input().upper()
# 내가 푼 풀이
"""
alpabet = [chr(_) for _ in range(65,91)]
count = []
for alpa in alpabet:
    c=s.count(alpa)
    if c==None:
        c=0
    count.append(c)


if count.count(max(count))>1:
    print("?")
else: print(alpabet[count.index(max(count))])
"""

unique_alpa=list(set(s))
count=[]
for alpa in unique_alpa:
    count.append(s.count(alpa))

if count.count(max(count))>1:
    print("?")
else:
    print(unique_alpa[count.index(max(count))])