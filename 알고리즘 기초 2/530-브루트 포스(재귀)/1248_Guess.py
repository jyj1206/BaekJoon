n=int(input())
s= [[-1 for i in range(n)] for j in range(n)]
sign=input()
cnt=0
for i in range(n):
  for j in range(i,n):
    if sign[cnt]=='+':
      s[i][j]=1
    elif sign[cnt]=='-':
      s[i][j]=-1
    else:
      s[i][j]=0
    cnt+=1

result=[0]*n

def check(idx):
  sum=0
  for i in range(idx,-1,-1):
    sum+=result[i]
    if s[i][idx] == 1 and sum<=0:
      return False
    elif s[i][idx] == 0 and sum!=0:
      return False
    elif s[i][idx]  == -1 and sum>=0:
      return False
  return True

def func(idx):
  if idx==n:
    return True
  
  if s[idx][idx]==0:
    result[idx]=0
    return check(idx) and func(idx+1)
  else:  
    for i in range(1,11):
      result[idx]=i*s[idx][idx]
      if check(idx) and func(idx+1):
        return True
    return False

func(0)
print(' '.join(map(str,result)))