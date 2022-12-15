import sys
input = sys.stdin.readline
n = int(input())
N= list(map(int,input().split()))
m = int(input())
M= list(map(int,input().split()))

## 집합
# insec_N_M = set(N) & set(M)
# for i in range(m):
#     if(M[i] in insec_N_M):
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

## dict
# _dict={}
# for i in range(n):
#     _dict[N[i]]=0

# for i in range(m):
#     if M[i] in _dict:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# # 이진탐색 재귀
# def binary_search(ary,n,start,end):
#     if start>end:
#         return 0
#     mid=(start+end)//2
#     if ary[mid]>n:
#         return binary_search(ary,n,start,mid-1)
#     elif ary[mid]<n:
#         return binary_search(ary,n,mid+1,end)
#     else:
#         return 1
# N.sort()
# for number in M:
#     if binary_search(N,number,0,n-1)==1:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")

#이진탐색 반복문 구현
def iter_binary_search(ary,n,start,end):
    while(start<=end):
        mid=(start+end)//2
        if ary[mid]>n:
            end=mid-1
        elif ary[mid]<n:
            start=mid+1
        else:
            return 1
    else:
        return 0

N.sort()
for number in M:
    if iter_binary_search(N,number,0,n-1)==1:
        print(1, end=" ")
    else:
        print(0, end=" ")