import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
lec = []
for _ in range(n):
  p, d = map(int, input().split())
  lec.append((d, p))
  
# 날짜를 기준으로 오름차순 정렬
lec.sort(key = lambda x : x[0])

h = []
for l in lec:
  # 보상을 오름차순 정렬
  heappush(h, l[1])
  
  # 현재 비교 날짜보다 더 많은 예약이 잡힌 경우
  if l[0] < len(h):
    heappop(h)

print(sum(h)) 


# 풀이 2 마지막날부터 확인
# import sys
# from heapq import heappop, heappush
# input = sys.stdin.readline
# n = int(input())
# lec = []
# max_d  = 0
# for _ in range(n):
#   p, d = map(int, input().split())
#   lec.append((d, p))
#   max_d = max(max_d, d)

# lec.sort(reverse=True)

# i = 0
# h = []
# ans = 0
# for day in range(max_d, 0, -1):
#   while i<n and day <= lec[i][0]:
#     heappush(h, -lec[i][1])
#     i+=1
  
#   if h:
#     p = heappop(h)
#     ans += -p
# print(ans)