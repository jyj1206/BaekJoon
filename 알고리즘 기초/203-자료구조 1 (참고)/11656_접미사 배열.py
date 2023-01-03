s = input()
ans=[]
for i in range(len(s)):
  ans.append(s[i:])
ans.sort()
for i in range(len(ans)):
  print(ans[i])