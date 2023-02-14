num = list(map(int, input()))
n_square_5 = [i**5 for i in range(10)]

ans = 0
for i in range(5):
  ans += n_square_5[num[i]]

print(ans)