import sys
input = sys.stdin.readline
t=int(input())
s=set()
for i in range(t):
  temp = input().rstrip().split()
  if len(temp)==1:
    if temp[0]=='all':
      s=set(range(1,21))
    else:
      s=set()
  else:
    oper, x = temp[0],int(temp[1])
    if oper=='add':
      s.add(x)
    elif oper=='remove':
      s.discard(x)
    elif oper=='check':
      if x in s:
        print(1)
      else:
        print(0)
    else:
      if x in s:
        s.discard(x)
      else:
        s.add(x)