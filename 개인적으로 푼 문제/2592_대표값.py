from collections import Counter
num = [int(input()) for _ in range(10)]

print(sum(num)//10)
print(Counter(num).most_common()[0][0])