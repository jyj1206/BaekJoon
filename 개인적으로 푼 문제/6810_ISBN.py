isbn = list(map(int,"9780921418"))
for i in range(3):
  isbn.append(int(input()))

ans = 0
for i in range(len(isbn)):
  if i%2==0:
    ans += isbn[i]
  else:
    ans += isbn[i]*3

print(f'The 1-3-sum is {ans}')