t = int(input())
ans=['advertise','does not matter','do not advertise']

for i in range(t):
  r,e,c=map(int,input().split())
  
  if e-r>c:
    print(ans[0])
  elif e-r==c:
    print(ans[1])
  else:
    print(ans[2])