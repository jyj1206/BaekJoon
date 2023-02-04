import sys
input = sys.stdin.readline

while True:
  s=input().strip()
  if s[0]=='#':
    break
  print(s[0],s[2:].lower().count(s[0]))