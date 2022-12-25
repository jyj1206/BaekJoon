import sys
input=sys.stdin.readline
t=int(input())
number = []
for i in range(t):
    number.append(int(input()))
# sort함수
# number.sort()
#for i in range(len(number)):    
#    print(i)
# 합병 정렬
# def merge_sort(arr):
#     if len(arr)<2:
#         return arr
    
#     mid = len(arr) //2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     l=h=0
#     sorted_arr=[]
#     while l<len(low_arr) and h<len(high_arr):
#         if low_arr[l]<high_arr[h]:
#             sorted_arr.append(low_arr[l])
#             l+=1
#         else:
#             sorted_arr.append(high_arr[h])
#             h+=1
#     #slice
#     #sorted_arr+=low_arr[l:] 
#     #sorted_arr+=high_arr[h:]
    
#     while l<len(low_arr):
#             sorted_arr.append(low_arr[l])
#             l+=1
#     while h<len(high_arr):
#             sorted_arr.append(high_arr[h])    
#             h+=1
#     return sorted_arr

# number=merge_sort(number)
# print(number)