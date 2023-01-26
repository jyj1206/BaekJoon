while True:
  n=input()
  if n=='0':
    break
  cnt=0
  for c in n:
    if c=='0':
      cnt+=4
    elif c=='1':
      cnt+=2
    else:
      cnt+=3
      
  print(cnt+len(n)+1)