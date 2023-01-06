N, m , M, T, R = map(int,input().split())

X=m
t,n=0,0
if M-X<T:
  print(-1)
else:
  while True:
    t+=1
    if X+T<=M:
      X+=T
      n+=1
    else:
      X-=R
      if X<m:
        X=m
        
    if n==N:
      print(t)
      break