import sys
input = sys.stdin.readline
k = int(input())
direction = []
length = []
for i in range(6):
    d,l = map(int,input().split())
    direction.append(d)
    length.append(l)

# 1, 3, 1, 3 처럼 방향이 번갈아 가며 등장하면 
for i in range(6):
    if direction[i]==direction[(i+2)%6] and direction[(i+1)%6]==direction[(i+3)%6]:
        break

one =  length[(i+1)%6]
another_one = length[(i+2)%6]

# 가장 긴변의 index
m=length.index(max(length))

# 가장 긴변, 가장 긴변과 인접한 변 중에 더 큰값
max_line = length[m]
adjust_max_line = max(length[(m-1)%6],length[(m+1)%6])

area=max_line*adjust_max_line-one*another_one

print(area*k)