import sys
input = sys.stdin.readline
n = int(input())
s = sum(map(int, input().split()))

print("yes" if s%3==0 else "no")