import sys
input = sys.stdin.readline
a,b= input().split()
a = map(int,a)
b = map(int,b)
print(sum(a)*sum(b))