arr = list(map(int, input()))

if sum(arr)%3==0:
  arr.sort(reverse = True)
  if arr[-1] == 0:
    print(''.join(map(str, arr)))
  else:
    print(-1)
else:
  print(-1)