n, m = map(int, input().split())
if n== 1:
  print(1)
elif n == 2:
  print(min(4, 1+(m-1)//2))
elif m < 7:
  print(min(4, m))
else:
  print(5 + (m - 7))


# 풀이 - 복잡함
# # 세로길이가 충분, 가로길이가 충분한 경우
# if n >= 3 and m >= 7:
#   print(5 + (m - 7))
# # 세로길이가 1인 경우
# elif n == 1:
#   print(1)
# # 세로 길이가 2인 경우
# elif n == 2:
#   # 가로 길이가 충분하면
#   if m >= 7:
#     print(4)
#   # 가로 길이가 충분하지 않으면
#   else:
#     print(1 + (m-1)//2)
# # 세로길이가 충분 한 경우
# else:
#   if m >= 4:
#     print(4)
#   else:
#     print(m)