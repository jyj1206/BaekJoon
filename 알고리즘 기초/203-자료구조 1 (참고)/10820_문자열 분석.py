while True:
  try:
    lo,up,nu,sp = 0, 0, 0, 0
    s=input()
    for char in s:
      if char.isdigit():
        nu+=1
      elif char.isspace():
        sp+=1
      elif char.isupper():
        up+=1
      else:
        lo+=1
    print(lo,up,nu,sp)
  except EOFError:
    break
## import sys 풀이
# import sys
# while(True):
#   s = sys.stdin.readline().rstrip('\n')
#   if not s:
#     break
#   lo,up,nu,sp = 0, 0, 0, 0
#   for char in s:
#     if char.isdigit():
#       nu+=1
#     elif char.isspace():
#       sp+=1
#     elif char.isupper():
#       up+=1
#     else:
#       lo+=1
#     # if char==' ':
#     #   sp+=1
#     # elif char.isdigit():
#     #   nu+=1
#     # else:
#     #   if ord(char)>=ord('A') and ord(char)<=ord('Z'):
#     #     up+=1
#     #   else:
#     #     lo+=1
  
#   sys.stdout.write(f"{lo} {up} {nu} {sp}\n")