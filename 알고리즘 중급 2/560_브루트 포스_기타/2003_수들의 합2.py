import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] += data[i-1]

data = [0] + data

i = 0
j = 1

result = 0

while i <= j and j <= n:
  if data[j] - data[i] == m:
    result += 1
    j += 1
  elif data[j] - data[i] > m:
    i += 1
  else:
    j += 1
  
  
print(result)


# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# i = 0
# j = 1

# result = 0

# while i <= j and j <= n:
#   subtotal = sum(data[i:j])
#   if subtotal== m:
#     result += 1
#     j += 1
#   elif subtotal > m:
#     i += 1
#   else:
#     j += 1
  
  
# print(result)