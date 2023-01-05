from collections import deque
n,m = map(int,input().split())
choice=list(map(int,input().split()))
_deque=deque([i for i in range(1,n+1)])

ans=0
for i in choice:
  while(True):
    if _deque[0]==i:
      _deque.popleft()
      break
    elif _deque.index(i)<=len(_deque)//2:
      while _deque[0]!=i:
        _deque.append(_deque.popleft())
        ans+=1
    else:
      while _deque[0]!=i:
        _deque.appendleft(_deque.pop())
        ans+=1
print(ans)
