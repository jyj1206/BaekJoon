import sys
input=sys.stdin.readline
n=int(input())
def star(n):
    if n==3:
        return ['***','* *','***']
    
    arr=star(n//3)
    stars=[]
    for i in arr:
        stars.append(i*3)
    
    for i in arr:
        stars.append(i+' '*(n//3)+i)

    for i in arr:
        stars.append(i*3)
    
    return stars

print('\n'.join(star(n)))







# stars =[ ['*' for j in range(n)] for i in range(n)]
# def del_star(n,x,y):
#     #타일의 크기
#     t=n//3

#     #없어질 타일 = 0
#     if t==0: return

#     #x,y좌표 기준으로 타일의 크기만큼 없애기
#     for i in range(x,x+t):
#         for j in range(y,y+t):
#             stars[i][j]=' '
    
#     #x,y좌표 기준으로 9가지 방향 좌표 재귀
#     for i in x-t+t//3,x+t//3, x+t+t//3:
#         for j in y-t+t//3,y+t//3, y+t+t//3:
#             del_star(t,i,j)

# del_star(n,n//3,n//3)

# for star in stars:
#     for s in star:
#         print(s, end="")
#     print()