import sys
input = sys.stdin.readline
s1,s2,s3 = map(int,input().split())
dice={}

for i in range(1,s1+1):
  for j in range(1,s2+1):
    for k in range(1,s3+1):
      sum=i+j+k
      if sum not in dice:
        dice[sum]=1
      else:
        dice[sum]+=1

max_value = 0
for key,value in dice.items():
  if max_value<value:
    max_value=value
    ans=key
print(ans)
# print(sorted(dice.items(), key=lambda x:(-x[1],x[0]))[0][0])
