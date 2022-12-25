import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    _dict = {}
    for i in range(n):
        name, kinds  = input().split()
        if kinds in _dict:
            _dict[kinds]+=1
        else:
            _dict[kinds]=1
    ans=1
    for n in _dict.values():
        ans*=n+1
    print(ans-1)