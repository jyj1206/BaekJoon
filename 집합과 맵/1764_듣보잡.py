import sys
input = sys.stdin.readline
n, m = map(int,input().split())
_dict={}
for i in range(n):
    _dict[input().strip()]=1
ans=[]
for j in range(m):
    temp=input().strip()
    if _dict.get(temp):
        ans.append(temp)
ans.sort()

print(len(ans))

for word in ans:
    print(word)