from math import pi
r = int(input())

#유클리드 기하학 원
print(f"{r**2*pi:.6f}")

#택시 기하학에서는 원이 마름모꼴
print(f"{(r*2)**2//2:.6f}")