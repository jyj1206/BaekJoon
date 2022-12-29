import sys
input =sys.stdin.readline
n = int(input())
stack=[]
for i in range(n):
  word = sys.stdin.readline().split()
  order=word[0]
  if order == 'push':
    stack.append(word[1])
  elif order == 'top':
    if not stack:
      print(-1)
    else:
      print(stack[-1])
  elif order == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  elif order == 'size':
    print(len(stack))
  else :
    if not stack:
      print(-1)
    else:
      print(stack.pop())



# linked list로 스택 구현
# class Node():
#   def __init__(self,data=None,next=None):
#     self.data=data
#     self.next=next
  
# class stack():
#   def __init__(self):
#     self.head=None
#     self.size=0

#   def push(self,data):
#     new_node=Node(data)
#     new_node.next=self.head
#     self.head=new_node
#     self.size+=1

#   def pop(self):
#     if self.size==0:
#       print(-1)
#     else:
#       value=self.head.data
#       self.head=self.head.next
#       print(value)
#       self.size-=1

#   def _size(self):
#     print(self.size)

#   def empty(self):
#     if self.size:
#       print(0)
#     else :
#       print(1)

#   def top(self):
#     if self.size==0:
#       print(-1)
#     else :
#       print(self.head.data)

# n = int(input())
# _stack=stack()
# for i in range(n):
#   s = input().strip()
#   if 'push' in s:
#     s, num=s.split()
    
#   if s=='push':
#     _stack.push(int(num))
#   elif s=='pop':
#     _stack.pop()
#   elif s=='top':
#     _stack.top()
#   elif s=='size':
#     _stack._size()
#   else:
#     _stack.empty()