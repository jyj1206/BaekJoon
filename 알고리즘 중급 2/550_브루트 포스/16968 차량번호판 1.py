s = input()
cnt = {'d' : 10, 'c' : 26}
answer = cnt[s[0]]
for i in range(1, len(s)):
  check = cnt[s[i]]
  if s[i-1] == s[i]:
    check -= 1
  answer *= check

print(answer)

# s = input()

# last = None
# answer = 1
# for c in s:
#   if c == 'd':
#     if last == 'd':
#       answer *= 9
#     else:
#       answer *= 10
#     last = 'd'
#   else:
#     if last == 'c':
#       answer *= 25
#     else:
#       answer *= 26
#     last = 'c'

# print(answer)