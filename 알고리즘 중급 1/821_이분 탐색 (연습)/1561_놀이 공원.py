import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rides = list(map(int, input().split()))

if n <= m:
  print(n)
else:
  # m개를 초과한 놀이기구를 타기 위한 최소 시간
  low = min(rides)
  high = max(rides) * n
  
  while low <= high:
    mid = (low + high) // 2
    
    cnt = m
    for i in range(m):
      cnt += mid // rides[i]
  
    if cnt >= n:
      high = mid - 1
    else:
      low = mid + 1
  
  # k분 때 n명 이상이 놀이기구를 탈 수 있음
  k = low
  
  # k-1분 때 탈 수 있는 사람의 수
  cnt = m
  for i in range(m):
    cnt += (k - 1) // rides[i]
  
  check = 0
  # k의 약수 중 (n - cnt)번째가 답
  for i in range(m):
    if (k%rides[i]==0) :
      check += 1
    
    if check == (n-cnt):
      print(i+1)
      break
  