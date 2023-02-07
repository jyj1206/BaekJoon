import sys
input = sys.stdin.readline
n = int(input())


stu = []
for i in range(n):
  name, *score = input().split()
  stu.append([name,*map(int, score)])

for s in sorted(stu,key = lambda x : (-x[1], x[2], -x[3], x[0])):
  print(s[0])
