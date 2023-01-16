n = int(input())
s = [0,1,0,0]
for i in range(n):
  x,y = map(int,input().split())
  s[x],s[y] = s[y],s[x]
  
print(s.index(1))