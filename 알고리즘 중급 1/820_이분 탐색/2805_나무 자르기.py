import sys
input = sys.stdin.readline

def cut_tree(size):
  cur_m = 0
  for tree in trees:
    temp = tree - size
    if temp > 0:
      cur_m += temp
  return cur_m
    

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = max(trees)

while left <= right:
  mid = (left + right)//2
  cur_m = cut_tree(mid)
  if cur_m >= m:
    left = mid+1
  else :
    right = mid-1
    

print(left-1)