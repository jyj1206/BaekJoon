import sys
input = sys.stdin.readline
_dict={
  '-':0,
  '\\':1,
  '(':2,
  '@':3,
  '?':4,
  '>':5,
  '&':6,
  '%':7,
  '/':-1
}
while True:
  s = input().strip()
  if s=='#':
    break
  s=s[::-1]
  ans=0
  for i in range(len(s)):
    ans+=(8**i)*_dict[s[i]]
  print(ans)