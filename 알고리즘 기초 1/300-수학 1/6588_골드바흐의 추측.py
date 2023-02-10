import sys
import math
input =sys.stdin.readline

max_num=1000001

prime=[False,False] + [True]*(max_num-2)

for i in range(2,int(math.sqrt(max_num))+1):
  if prime[i]:
    for j in range(i+i,max_num,i):
      prime[j]=False


while(True):
  n=int(input())
  if n==0: 
    break

  for i in range(3,n//2+1,2):
    if prime[i] and prime[n-i]:
      print(f'{n} = {i} + {n-i}')
      break
  else:
    print('Goldbach\'s conjecture is wrong.')
