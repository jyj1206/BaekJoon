def func(num):
    for s in str(num):
        num+=int(s)
    return num

numbers = list(range(1,10001))

for i in range(1,10001):
    a=func(i)
    if a in numbers:
        numbers.remove(a)

for number in numbers:
    print(number)