import sys
input = sys.stdin.readline
n,m = map(int,input().split())
_dict={}
for i in range(n):
    word=input().strip()
    _dict[word]=i+1
    _dict[i+1]=word

for i in range(m):
    quest=input().strip()
    if quest.isdigit()==True:
        print(_dict[int(quest)])
    else:
        print(_dict[quest])