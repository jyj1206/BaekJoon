import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))

set_numbers=list(set(numbers))
set_numbers.sort()

_dict = {}
for i in range(len(set_numbers)):
    _dict[set_numbers[i]]=i

for i in range(n):
    print(_dict[numbers[i]],end = ' ')