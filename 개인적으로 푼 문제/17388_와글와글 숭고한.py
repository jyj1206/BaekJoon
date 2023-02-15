s, k, h = map(int, input().split())
if s + k + h >= 100:
  print('OK')
else:
  min_value = min([s,k,h])
  if min_value == s:
    print("Soongsil")
  elif min_value == k:
    print("Korea")
  else:
    print("Hanyang")