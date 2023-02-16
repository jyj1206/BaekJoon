# 풀이 1
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
  for y in range(-999, 1000):
    if (a*x+b*y == c) and (d*x+e*y == f):
      print(x, y)
      break


# 풀이 2
# a, b, c, d, e, f = map(int, input().split())
# x = (e*c-b*f) // (a*e-d*b)
# y = (d*c-a*f) // (d*b-a*e)

# print(x, y)
