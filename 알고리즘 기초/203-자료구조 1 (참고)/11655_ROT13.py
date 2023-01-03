s = list(map(str,input()))
for i in range(len(s)):
  if s[i].islower():
    s[i] = chr((ord(s[i])+13-ord('a'))%26+ord('a'))
  if s[i].isupper():
    s[i] = chr((ord(s[i])+13-ord('A'))%26+ord('A'))
  print(s[i],end='')