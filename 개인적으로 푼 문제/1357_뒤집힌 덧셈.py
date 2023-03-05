def reverse(n):
  return int(n[::-1])
x, y = input().split()
print(int(reverse(str(reverse(x) + reverse(y)))))