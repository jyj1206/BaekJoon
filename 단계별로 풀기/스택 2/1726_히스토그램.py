import sys
input = sys.stdin.readline
n = int(input())
chart = [int(input()) for _ in range(n)]

stack=[]
ans=0

for i, cur_h in enumerate(chart):
  last=i
  while stack and stack[-1][0]>cur_h:
    h, idx = stack.pop()
    ans = max(ans,h*(i-idx))
    last= idx
  
  # 스택이 있으면서, 현재 top에 있는 차트의 높이랑 같으면
  if stack and stack[-1][0]==cur_h:
    continue
  else :
    stack.append((cur_h,last))

while stack:
  h,idx=stack.pop()
  ans=max(ans,h*(n-idx))

print(ans)



# 시간 초과
# for i in range(n):
#   # 높이가 0인 히스토그램
#   cur_h = chart[i]
#   if cur_h==0:
#     while stack:
#       h,w=stack.pop()
#       ans=max(ans,h*w)
  
#   else:
#     last=0
    
#     while stack and stack[-1][0]>cur_h:
#       h,w = stack.pop()
#       ans=max(ans,h*w)
#       last = w
#     # 스택이 있으면
#     if stack:
#       # 현재 높이랑 같은 것이 있으면
#       if stack[-1][0]==cur_h:
#         h, w=stack.pop()
#         register.append((h,w+1))
#       # 없는 경우 현재 높이보다 큰 것들 중에 가장 작은 것에 너비+1
#       else:
#         register.append((cur_h,last+1))
      
#       # 스택에 남은 것들(현재 높이보다 작은 것들), 모두+1
#       while stack:
#         h, w = stack.pop()
#         register.append((h,w+1))
      
#       # 계산된것들 다시 스택에 옮김
#       while register:
#         stack.append(register.pop())
      
#     # 스택이 비었으면
#     else:
#       stack.append((cur_h,last+1))

# # 스택에 남은 것들 계산
# while stack:
#   h,w=stack.pop()
#   ans=max(ans,h*w)

# print(ans)