import sys
input = sys.stdin.readline
vowel=set('aeiouAEIOU')
while True:
  s=input().strip()
  if s=='#':
    break
  cnt=0
  for char in s:
    if char in vowel:
      cnt+=1
  print(cnt)