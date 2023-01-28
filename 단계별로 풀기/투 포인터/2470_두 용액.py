import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

dist=abs(arr[0]+arr[-1])
ans_i=0
ans_j=len(arr)-1
i=0
j=len(arr)-1

while True:
  mix=arr[i]+arr[j]
  
  if abs(mix)<dist:
    dist = abs(mix)
    ans_i=i
    ans_j=j
    
  if mix>0:
    j-=1
  elif mix<0:
    i+=1
  else:
    break
  
  if i==j:
    break

print(arr[ans_i],arr[ans_j])
