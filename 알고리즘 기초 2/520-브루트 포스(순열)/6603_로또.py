from itertools import combinations
import sys
input = sys.stdin.readline

while(True):
  nums=list(map(int,input().split()))
  if nums[0]==0:
    break
  for ans in combinations(nums[1:],6):
    print(' '.join(map(str,ans)))
  print()