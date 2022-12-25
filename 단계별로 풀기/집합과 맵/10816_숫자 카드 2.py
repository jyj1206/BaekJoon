import sys
input = sys.stdin.readline

number=[]
number2=[]

n=int(input())
number=list(map(int,input().split()))

m=int(input())
number2=list(map(int,input().split()))

_dict={}

for i in number:
    if i in _dict:
        _dict[i]+=1
    else : _dict[i]=1

for i in number2:
    if i in _dict:
        print(_dict[i], end=' ')
    else : print(0, end = ' ')