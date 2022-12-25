import sys
input = sys.stdin.readline
n = int(input())
cnt = [0]*10001
for i in range(n):
    n = int(input())
    cnt[n]+=1

for i in range(10001):
    if cnt[i] !=0:
        for j in range(cnt[i]):
            print(i)