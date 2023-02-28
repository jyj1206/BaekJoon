l, p = map(int, input().split())
print(*map(lambda x : int(x) - l*p, input().split()))