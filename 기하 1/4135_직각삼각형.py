import sys
input = sys.stdin.readline
while(True):
    three_point = list(map(int,input().split()))
    if sum(three_point)==0:
        break
    three_point.sort()
    if three_point[0]**2+three_point[1]**2==three_point[2]**2:
        print('right')
    else:
        print('wrong')
