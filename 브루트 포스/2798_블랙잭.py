import sys
input = sys.stdin.readline
n, m = map(int,input().split())
card = list(map(int,input().split()))
set_three = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k]<=m:
                set_three.append(card[i]+card[j]+card[k])

print(max(set_three))