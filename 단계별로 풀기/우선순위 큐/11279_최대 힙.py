# 직접 구현
import sys
input = sys.stdin.readline

class MaxHeap:
  def __init__(self):
    self.data=[None]
  
  def insert(self,item):
    self.data.append(item)
    # 마지막 item 위치
    i=len(self.data)-1
    while i>1:
      # 현재 노드가 부모 노드보다 더크면  
      if self.data[i]>self.data[i//2]:
        self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
        i=i//2
      else:
        break
  
  def remove(self):
    if len(self.data)>1:
      self.data[1],self.data[-1]=self.data[-1],self.data[1]
      data = self.data.pop()
      self.maxHeapify(1)      
    else:
      data=None
    return data
  
  def maxHeapify(self,i):
    last = len(self.data)-1
    left = 2*i
    right = (2*i)+1
    max_index=i
    
    if left<=last and self.data[max_index]<self.data[left]:
      max_index=left
    if right<=last and self.data[max_index]<self.data[right]:
      max_index=right
    
    if i!=max_index:
      self.data[i], self.data[max_index] = self.data[max_index], self.data[i]
      self.maxHeapify(max_index)

n = int(input())
h = MaxHeap()
for i in range(n):
  x = int(input())
  if x==0:
    data=h.remove()
    if data!=None:
      print(data)
    else:
      print(0)
  else:
    h.insert(x)


# heapq 라이브러리
# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())

# h=[]

# for i in range(n):
#   x = int(input())
#   if x==0:
#     if not h:
#       print(0)
#     else:
#       print(-heapq.heappop(h))
#   else:
#     heapq.heappush(h,-x)