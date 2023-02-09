import sys
input = sys.stdin.readline
n = int(input())
init = list(map(int,input().strip()))
target = list(map(int,input().strip()))

def change(bulb, i):
  if i == 0:
    bulb[i] = 1 - bulb[i]
    bulb[i+1] = 1 - bulb[i+1]
  elif i == len(bulb)-1:
    bulb[i-1] = 1 - bulb[i-1]
    bulb[i] = 1 - bulb[i]
  else:
    bulb[i-1] = 1 - bulb[i-1]
    bulb[i] = 1 - bulb[i]
    bulb[i+1] = 1 - bulb[i+1]


case_1 = init[:]
change(case_1, 0)
case_2 = init[:]

cnt_1 = 1
for i in range(1, n):
  if target[i-1] != case_1[i-1] :
    change(case_1, i)
    cnt_1 += 1

cnt_2 = 0
for i in range(1, n):
  if target[i-1] != case_2[i-1] :
    change(case_2, i)
    cnt_2 += 1

if case_1 == target and case_2 == target:
  print(min(cnt_1,cnt_2))
elif case_1 == target:
  print(cnt_1)
elif case_2 == target:
  print(cnt_2)
else:
  print(-1)
