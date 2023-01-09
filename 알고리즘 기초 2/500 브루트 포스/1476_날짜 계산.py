e,s,m = map(int,input().split())

y=0
cnt=1
while(True):
  if y%15+1==e and y%28+1==s and y%19+1==m:
    print(cnt)
    break
  cnt+=1
  y+=1