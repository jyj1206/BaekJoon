while(True):
  n=int(input())
  if n==-1:
    break
  ans=[]
  for i in range(1,n):
    if n%i==0:
      ans.append(i)
      
  if n==sum(ans):
    s = ' + '.join(map(str,ans))
    print(f'{n} = {s}')
  else:
    print(f'{n} is NOT perfect.')