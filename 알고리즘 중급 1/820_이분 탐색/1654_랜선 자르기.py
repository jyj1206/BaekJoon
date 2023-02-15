import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lans = []
for _ in range(k):
  lans.append(int(input()))

max_lan = max(lans)

def find_k(base):
  n = 0
  for lan in lans:
    n += lan//base
  return n
  
def upperbound():
  left = 1
  right = max_lan+1
  while left < right:
    mid = (left + right)//2
    cur_n = find_k(mid)
    
    if cur_n < n :
      right = mid
    else:
      left = mid +1
  return left

print(upperbound()-1)