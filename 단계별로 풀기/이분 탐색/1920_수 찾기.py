import sys
input = sys.stdin.readline
n = int(input())
num=list(map(int,input().split()))
m = int(input())
case=list(map(int,input().split()))

def binary_search(target):
  left=0
  right=len(num)-1
  while(left<=right):
    mid=(left+right)//2
    if num[mid]==target:
      return 1
    elif num[mid]>target:
      right=mid-1
    else:
      left=mid+1
  return 0

def merge(left,right):
  l=r=0
  merged_arr=[]
  while l<len(left) and r<len(right):
    if left[l]<right[r]:
      merged_arr.append(left[l])
      l+=1
    else:
      merged_arr.append(right[r])
      r+=1
  merged_arr+=left[l:]
  merged_arr+=right[r:]
  return merged_arr

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  sorted_left=merge_sort(left)
  sorted_right=merge_sort(right)
  return merge(sorted_left,sorted_right)

num=merge_sort(num)

for i in case:
  print(binary_search(i))

# sort 함수
# num.sort()

# 재귀
# def binary_search(left,right,target):
#   if left>right:
#     return 0
#   mid=(left+right)//2
#   if num[mid]==target:
#     return 1
#   elif num[mid]>target:
#     return binary_search(left,mid-1,target)
#   else:
#     return binary_search(mid+1,right,target)    
# num.sort()
# for i in case:
#   print(binary_search(0,n-1,i))