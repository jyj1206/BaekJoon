import sys
input = sys.stdin.readline

class MinHeap:
  def __init__(self):
    self.data=[None]
  
  def insert(self,data):
    self.data.append(data)
    i=len(self.data)-1
    while i>1:
      if self.data[i]<self.data[i//2]:
        self.data[i],self.data[i//2] = self.data[i//2], self.data[i]
        i//=2
      else:
        break
  
  def delete(self):
    if len(self.data)>1:
      self.data[1],self.data[-1] = self.data[-1],self.data[1]
      data=self.data.pop()
      self.minHeapify(1)
    else:
      data=None
    return data

  def minHeapify(self,i):
    last=len(self.data)-1
    left = i*2
    right = i*2+1
    min_idx=i
    if left<=last and self.data[min_idx]>self.data[left]:
      min_idx=left
    if right<=last and self.data[min_idx]>self.data[right]:
      min_idx=right
    
    if min_idx!=i:
      self.data[min_idx], self.data[i] = self.data[i], self.data[min_idx]
      self.minHeapify(min_idx)

n = int(input())
h = MinHeap()
for i in range(n):
  x = int(input())
  if x==0:
    data=h.delete()
    if data:
      print(data)
    else:
      print(0)
  else:
    h.insert(x)

# heapq 라이브러리 사용
# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline

# n = int(input())

# h=[]
# for i in range(n):
#   x = int(input())
#   if x==0:
#     if not h:
#       print(0)
#     else:
#       print(heappop(h))
#   else:
#     heappush(h,x)