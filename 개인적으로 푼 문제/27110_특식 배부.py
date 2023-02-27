n = int(input())
a, b, c = map(int, input().split())
print(min(a, n) + min(b, n) + min(c, n))