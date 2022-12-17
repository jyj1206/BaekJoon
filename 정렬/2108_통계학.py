import sys
from collections import Counter
input = sys.stdin.readline
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))

##sort()함수로 정렬
#num.sort()

#병합 정렬
def merge(left,right):
    l=r=0
    l_last = len(left)
    r_last = len(right)
    sorted_ary=[]
    while l<l_last and r<r_last:
        if left[l]<right[r]:
            sorted_ary.append(left[l])
            l+=1
        else:
            sorted_ary.append(right[r])
            r+=1
    sorted_ary+=left[l:]
    sorted_ary+=right[r:]
    return sorted_ary
            
def merge_sort(ary):
    if len(ary)<=1:
        return ary
    mid = len(ary)//2
    left_ary=ary[:mid]
    right_ary=ary[mid:]
    left_sorted_ary=merge_sort(left_ary)
    right_sorted_ary=merge_sort(right_ary)
    return merge(left_sorted_ary,right_sorted_ary)

num=merge_sort(num)

# 출력
print(round(sum(num)/n))
print(num[n//2])
cnt=Counter(num)
cnt_tuple_list=cnt.most_common()
max_cnt=cnt_tuple_list[0][1]
mode = []
for cnt_tuple in cnt_tuple_list:
    if cnt_tuple[1]==max_cnt:
        mode.append(cnt_tuple[0])
if len(mode)>1:
    print(mode[1])
else :
    print(mode[0])

print(max(num)-min(num))