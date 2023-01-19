import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def preorder(cur_node):
  if cur_node!='.':
    print(cur_node,end='')
    preorder(tree[cur_node][0])
    preorder(tree[cur_node][1])

def inorder(cur_node):
  if cur_node!='.':
    inorder(tree[cur_node][0])
    print(cur_node,end='')
    inorder(tree[cur_node][1])

def postorder(cur_node):
  if cur_node!='.':
    postorder(tree[cur_node][0])
    postorder(tree[cur_node][1])
    print(cur_node,end='')

tree={}
n = int(input())
for i in range(n):
  value, left, right = input().split()
  tree[value]=[left,right]

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')