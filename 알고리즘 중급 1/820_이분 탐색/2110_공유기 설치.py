import sys
input = sys.stdin.readline
n, c = map(int, input().split())

house = [int(input()) for _ in range(n)]

house.sort()

start = 1
end = house[-1] - house[0]

while start <= end :
  # 공유기 사이의 최대 거리
  mid = (start + end) // 2
  cur = house[0]
  cnt = 0
  for i in range(1, n):
    if house[i] - cur >= mid:
      cnt += 1
      cur = house[i]

  # 설치 된 개수가 설치해야 할 개수 보다 작은 경우 간격을 줄여줘야함
  if cnt < c:
    end = mid -1
  else:
    start = mid + 1

print(start - 1)