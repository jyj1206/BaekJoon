a = list(range(1,31))
for i in range(28):
    a.remove(int(input()))
print(min(a))
print(max(a))