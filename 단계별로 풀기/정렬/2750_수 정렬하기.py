import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
t=int(input())
number = []
for i in range(t):
    number.append(int(input()))

# 퀵 정렬
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1 : ]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) 

for num in quick_sort(number):
    print(num)


# sort, sorted 시간복잡도 : O(nlogn)
#number=sorted(number)

# 버블 정렬 시간복잡도 : O(n^2)
# for i in range(len(number)-1,0,-1):
#     for j in range(i):
#         if number[j]>number[j+1]:
#             number[j],number[j+1] = number[j+1],number[j]

# 선택 정렬 시간복잡도 : O(n^2)
#for i in range(len(number)-1):
#    min_index=i
#    for j in range(i+1,len(number)):
#        if number[j]<number[min_index]:
#            min_index=j
#    number[i],number[min_index]=number[min_index],number[i]

# # 삽입 정렬 시간복잡도 : O(n^2)
# for i in range(1, number):
#     for j in range(i,0,-1):
#         if number[j-1]>number[i]:
#             number[j-1],number[i]=number[i],number[j-1]
#         else:
#             break
# for n in number:
#     print(n)

# # 퀵 정렬
# def check_pivot(ary,left,right):
#     pivot = ary[(left+right)//2]
#     l=left
#     r=right
#     while(l<=r):
#         while ary[l] < pivot:
#             l+=1
#         while ary[r] > pivot:
#             r-=1
#         if l<=r:
#             ary[l],ary[r]=ary[r],ary[l]
#             l+=1
#             r-=1
#     return l

# def quick_sort(ary,left,right):
#     if left<right:
#         pivot = check_pivot(ary,left,right)
#         quick_sort(ary,left,pivot-1)
#         quick_sort(ary,pivot,right)
#     else : return

# quick_sort(number,0,len(number)-1)
# for num in number:
#     print(num)