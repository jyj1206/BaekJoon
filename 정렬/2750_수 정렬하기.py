t=int(input())
number = []
for i in range(t):
    number.append(int(input()))
# sort, sorted 시간복잡도 :O(nlogn)
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

# 삽입 정렬 시간복잡도 : O(n^2)
for i in range(1, number):
    for j in range(i,0,-1):
        if number[j-1]>number[i]:
            number[j-1],number[i]=number[i],number[j-1]
        else:
            break

for n in number:
    print(n)