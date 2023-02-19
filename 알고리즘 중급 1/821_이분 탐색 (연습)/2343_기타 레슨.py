import sys
def get_cnt(size):
  time = 0
  cnt = 0
  for video in videos:
    if time + video > size:
      time = 0
      cnt += 1
    time += video
  if time > 0 :
    cnt += 1
  return cnt

def lower_bound():
  start = max(videos)
  end = sum(videos)
  
  while start <= end:
    mid = (start + end) // 2
    cnt = get_cnt(mid)
    
    if cnt <= m:
      end = mid - 1
    else:
      start = mid + 1
  
  return start

input = sys.stdin.readline
n, m = map(int, input().split())
videos = list(map(int, input().split()))
print(lower_bound())