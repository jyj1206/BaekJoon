alpa = [0]*26
s = input()

for char in s:
  alpa[ord(char)-ord('a')]+=1

alpa=list(map(str,alpa))
print(' '.join(alpa))