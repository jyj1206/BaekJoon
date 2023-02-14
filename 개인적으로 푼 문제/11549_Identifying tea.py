import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))

print(num.count(n))