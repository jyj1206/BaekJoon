from collections import deque
a, b, c = map(int,input().split())
# 전체 돌 개수는 고정임
total = a + b + c

visited=[[0 for j in range(total+1)] for i in range(total+1)]
def bfs():
  q = deque()
  x = min(a,b,c)
  y = max(a,b,c)
  visited[x][y]=1
  q.append((x,y))
  while q:
    cur_a,cur_b=q.popleft()
    cur_c=total-cur_a-cur_b
    if cur_a==cur_b==cur_c:
      print(1)
      return
    for x, y in (cur_a,cur_b),(cur_b,cur_c),(cur_c,cur_a):
      if x==y:
        continue
      elif x>y:
        x-=y
        y+=y
      else:
        y-=x
        x+=x
      z = total-x-y
      nx=min(x,y,z)
      ny=max(x,y,z)
      if not visited[nx][ny]:
        visited[nx][ny]=1
        q.append((nx,ny))
  
  print(0)
  

# 전체 돌 개수가 3의 배수가 아니면 조건 만족 불가
if total%3!=0:
  print(0)
else:
  bfs()


# 비효율적인 풀이
# visited=set()

# def next_step(s1,s2):
#   if s1>s2:
#     s1=s1-s2
#     s2*=2
#   else:
#     s2=s2-s1
#     s1*=2
#   return s1, s2
  
# def bfs():
#   visited.add((a,b,c))
#   q = deque([(a,b,c)])
#   while q:
#     cur_a,cur_b,cur_c=q.popleft()
#     if cur_a==cur_b==cur_c:
#       return 1
    
#     if cur_a!=cur_b:
#       n_a,n_b=next_step(cur_a,cur_b)
#       if (n_a,n_b,cur_c) not in visited:
#         q.append((n_a,n_b,cur_c))
#         visited.add((n_a,n_b,cur_c))
        
#     if cur_b!=cur_c:
#       n_b,n_c=next_step(cur_b,cur_c)
#       if (cur_a,n_b,n_c) not in visited:
#         q.append((cur_a,n_b,n_c))
#         visited.add((cur_a,n_b,n_c))
        
#     if cur_c!=cur_a:
#       n_c,n_a=next_step(cur_c,cur_a)
#       if (n_a,cur_b,n_c) not in visited:
#         q.append((n_a,cur_b,n_c))
#         visited.add((n_a,cur_b,n_c))

#   return 0

# print(bfs())