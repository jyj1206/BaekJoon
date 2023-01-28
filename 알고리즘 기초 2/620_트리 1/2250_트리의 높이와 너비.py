import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree={}

parent=[-1]*(n+1)
for i in range(n):
  node, left, right= map(int,input().split())
  tree[node]=(left,right)
  if left!=-1:
    parent[left]=node
  if right!=-1:
    parent[right]=node

for i in range(1,n+1):
  if parent[i]==-1:
    root=i
    break

result={}
cnt=1
def inorder(cur_node,level):
  global cnt
  if cur_node!=-1:
    inorder(tree[cur_node][0],level+1)
    if level not in result:
      result[level]=[cnt]
    else:
      result[level].append(cnt)
    cnt+=1
    inorder(tree[cur_node][1],level+1)
inorder(root,1)

ans_level=0
max_width=0
for each_level in sorted(result.items()):
  level, each_node=each_level
  width=each_node[-1]-each_node[0]+1
  if max_width<width:
    ans_level=level
    max_width=width
    
print(ans_level,max_width)