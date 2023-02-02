import sys
import string
input = sys.stdin.readline


n = input().strip()

m = int(input())

words=[]
for i in range(m):
  words.append(input().strip())

if m==1:
  print(words[0])
else:
  l,o,v,e=0,0,0,0
  l = n.count('L')
  o = n.count('O')
  v = n.count('V')
  e = n.count('E')
  
  ans=[]
  for word in words:
    L=word.count('L')+l
    O=word.count('O')+o
    V=word.count('V')+v
    E=word.count('E')+e
    
    value=((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    ans.append((value,word))
  
  ans.sort(key=lambda x : (-x[0],x[1]))
  
  print(ans[0][1])