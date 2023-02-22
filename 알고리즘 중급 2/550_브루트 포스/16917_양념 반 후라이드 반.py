a, b, c, x, y = map(int, input().split())

if a + b  < 2 * c:
  print(a * x + b * y)
else:
  set_cnt = min(x, y)
  case_1 = c * 2 * set_cnt + a * (x - set_cnt) + b * (y - set_cnt)
  case_2 = c * max(x, y) * 2
  print(min(case_1, case_2))