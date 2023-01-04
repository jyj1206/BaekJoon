from collections import deque
n= int(input())
num = deque([i+1 for i in range(n)])

while(len(num)!=1):
  num.popleft()
  num.append(num.popleft())
print(num[-1])