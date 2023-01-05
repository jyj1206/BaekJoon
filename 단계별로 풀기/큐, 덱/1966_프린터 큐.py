import sys
from collections import deque
input = sys.stdin.readline
t= int(input())
for i in range(t):
  n,m=map(int,input().split())
  queue=deque(map(int,input().split()))
  idx=deque([i for i in range(n)])
  
  result=1
  while queue:
    if queue[0]==max(queue):
      queue.popleft()
      index=idx.popleft()
      if index==m:
        print(result)
        break
      result+=1
    else:
      queue.append(queue.popleft())
      idx.append(idx.popleft())



  # result=[]
  # max_value=max(text)
  # while queue:
  #   if text[queue[0]]==max_value:
  #     text[queue[0]]=-1
  #     result.append(queue.popleft())
  #     max_value=max(text)
  #   else:
  #     queue.append(queue.popleft())
  
  # print(result.index(m)+1)