import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
  s = input().strip()
  cnt = 0
  v = 0
  vowel = set('AEIOUaeiou')
  for c in s:
    if c.isalpha():
      cnt+=1
      if c in vowel:
        v+=1
  print(cnt-v, v)