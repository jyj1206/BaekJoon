from collections import deque
n,k = map(int,input().split())

people = deque()
for i in range(1, n+1): people.append(i)
result = []

while people:
  for _ in range(k-1):
    people.append(people.popleft())

  result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))



# 풀이 수정
#queue=deque()
#h = [i for i in range(1,n+1)]
# i=k-1
# while(len(queue)!=n):
#   i=i%len(h)
#   queue.append(h.pop(i))
#   i-=1
#   i+=k

# print('<', end='')
# for i in range(n):
#   s=queue.popleft()
#   if i==n-1:
#     print(s, end='')
#   else:
#     print(s, end=', ')
# print('>')