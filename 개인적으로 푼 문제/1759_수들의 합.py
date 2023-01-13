s = int(input())
n = 1
result=0

while(True):
  result+=n
  if result>s:
    print(n-1)
    break
  n+=1




#풀이 1
# while n * (n + 1) // 2 <= s:
#     n += 1
# print(n - 1)