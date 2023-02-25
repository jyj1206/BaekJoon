# 풀이 1 - 수정

# 풀이 2
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# cctv = []
# office = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#   for j in range(m):
#     if 1 <= office[i][j] <= 5:
#       cctv.append((i, j))


# def up(x, y, office):
#   while 0 <= x - 1 and office[x - 1][y] != 6:
#     if office[x - 1][y] == 0:
#       office[x - 1][y] = '#'    
#     x = x - 1
#   return office

# def down(x, y, office):
#   while x + 1 < n and office[x + 1][y] != 6:
#     if office[x + 1][y] == 0:
#       office[x + 1][y] = '#'    
#     x = x + 1
#   return office

# def left(x, y, office):
#   while 0 <= y - 1 and office[x][y - 1] != 6:
#     if office[x][y - 1] == 0:
#       office[x][y - 1] = '#'    
#     y = y - 1
#   return office

# def right(x, y, office):
#   while y + 1 < m and office[x][y + 1] != 6:
#     if office[x][y + 1] == 0:
#       office[x][y + 1] = '#'    
#     y = y + 1
#   return office

# def count():
#   return office.count(0)

# # idx : cctv 번호
# def dfs(idx, office):
#   global blind_spot
#   if idx == len(cctv):
#     cnt = sum([row.count(0) for row in office])
#     if cnt == 0:
#       print(0)
#       exit()
#     blind_spot = min(blind_spot, cnt)
#     return

#   x, y = cctv[idx]
#   if office[x][y] == 1:
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, up(x, y, next_office))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, down(x, y, next_office))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, left(x, y, next_office))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, right(x, y, next_office))
    
#   elif office[x][y] == 2:
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, down(x, y, up(x, y, next_office)))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, right(x, y, left(x, y, next_office)))
    
#   elif office[x][y] == 3:
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, right(x, y, up(x, y, next_office)))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, down(x, y, right(x, y, next_office)))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, left(x, y, down(x, y, next_office)))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, up(x, y, left(x, y, next_office)))
    
#   elif office[x][y] == 4:
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, down(x, y, right(x, y, up(x, y, next_office))))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, left(x, y, down(x, y, right(x, y, next_office))))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, up(x, y, left(x, y, down(x, y, next_office))))
    
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, right(x, y, up(x, y, left(x, y, next_office))))
#   else:
#     next_office = [row[:] for row in office]
#     dfs(idx + 1, right(x, y, left(x, y, down(x, y, up(x, y, next_office)))))
    

# blind_spot = int(1e9)
# dfs(0, office)
# print(blind_spot)