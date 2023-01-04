from collections import deque
n, k = map(int,input().split())
num = deque([i+1 for i in range(n)])

ans=[]
while(num):
  for i in range(k-1):
    num.append(num.popleft())
  ans.append(num.popleft())

print(str(ans).replace('[','<').replace(']','>'))
