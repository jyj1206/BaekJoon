import sys

def check(size) :
  # 초기화
  cnt = 0
  cur_max = min_v
  cur_min = max_v
  for i in range(n):
    cur_max = max(cur_max, array[i])
    cur_min = min(cur_min, array[i])
    
    # 현재 구간의 점수가 size(구간의 점수의 최댓값)보다 더 커져버리면
    if cur_max - cur_min > size:
      cur_max = array[i]
      cur_min = array[i]
      cnt += 1
      
  # for문 탈출 후 마지막 구간 count
  cnt += 1
  return cnt

input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))

max_v = max(array)
min_v = min(array)
low = 0
high = max_v - min_v

while low <= high:
  mid = (low + high) // 2
  # 구간을 나누는 것이 가능하면, mid 값 감소 시키기 (더 작은 최댓값이 가능)
  if check(mid) <= m:
    high = mid - 1
  # 구간을 나누는 것이 불가능하면, mid 값 증가 시키기
  else:
    low = mid + 1

print(low)