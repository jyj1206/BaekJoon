S=input().upper()
n = [chr(i) for i in range(65,91)]
for x in n:
    print(S.find(x), end=' ')