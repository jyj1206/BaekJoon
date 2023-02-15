import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

idx = [0] * (n+1)
for i in range(n):
  idx[inorder[i]] = i

def dq(in_start, in_end, post_start, post_end):
  if in_start > in_end:
    return
  parent = postorder[post_end]
  preorder.append(parent)
  mid = idx[parent]
  # 왼쪽 자식 개수
  left_child = mid - in_start
  # 오른쪽 자식 개수
  right_child = in_end - mid
  dq(in_start, mid-1, post_start, post_start + left_child -1)
  dq(mid+1, in_end, post_start + left_child, post_start + left_child + right_child - 1)
  
dq(0, n-1, 0, n-1)
print(*preorder)