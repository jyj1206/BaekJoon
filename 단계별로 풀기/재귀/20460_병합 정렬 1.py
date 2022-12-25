import sys
import math
input = sys.stdin.readline
n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = []
def merge_sort(A):
    if len(A)==1:
        return A
    mid = math.ceil(len(A)/2)
    low_list=merge_sort(A[:mid])
    high_list=merge_sort(A[mid:])
    merged_list=merge(low_list,high_list)
    return merged_list

def merge(low_list,high_list):
    l=h=0
    merged_list=[]
    while l<len(low_list) and h<len(high_list):
        if low_list[l]<high_list[h]:
            merged_list.append(low_list[l])
            l+=1
        else:
            merged_list.append(high_list[h])
            h+=1
        ans.append(merged_list[-1])
    
    while l<len(low_list):
        merged_list.append(low_list[l])
        l+=1
        ans.append(merged_list[-1])   
    
    while h<len(high_list):
        merged_list.append(high_list[h])
        h+=1
        ans.append(merged_list[-1])

    return merged_list

merge_sort(A)
if k>len(ans):
    print(-1)
else:    
    print(ans[k-1])