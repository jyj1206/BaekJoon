# 풀이 1 - merge sort
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)

def merge(left, right):
  l = 0
  r = 0
  sorted_arr = []
  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      sorted_arr.append(left[l])
      l+=1
    else:
      sorted_arr.append(right[r])
      r+=1
  sorted_arr += left[l:]
  sorted_arr += right[r:]
  return sorted_arr

result = merge_sort(num)
print(result[k-1])
# 풀이2 - sorted 함수
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# num = list(map(int, input().split()))
# print(sorted(num)[k-1])