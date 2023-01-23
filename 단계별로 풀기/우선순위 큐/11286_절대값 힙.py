# 풀이 1
# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
# n = int(input())

# h=[]
# for i in range(n):
#   x = int(input())
#   if x==0:
#     if not h:
#       print(0)
#     else:
#       print(heappop(h)[1])
#   else:
#     heappush(h,(abs(x),x))

#풀이 2
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())

# 양수 저장
min_heap=[]
# 음수 저장
max_heap=[]

for i in range(n):
  x = int(input())
  if x<0:
    heappush(max_heap,-x)
  elif x>0:
    heappush(min_heap,x)
  else:
    if not min_heap and not max_heap:
      print(0)
    elif max_heap and not min_heap:
      print(-heappop(max_heap))
    elif min_heap and not max_heap:
      print(heappop(min_heap))
    else:
      if min_heap[0]>=max_heap[0]:
        print(-heappop(max_heap))
      else:
        print(heappop(min_heap)) 