import sys
input = sys.stdin.readline
r,c = map(int,input().split())

checker=[]
pattern = ['WB','BW']
# 0 : W 시작, 1 : B 시작
pattern[0] = pattern[0]*4
pattern[1] = pattern[1]*4


for i in range(r):
    checker.append(input().strip())

result=[]
for i in range(r-8+1):
    for j in range(c-8+1):
        w=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if k%2==0 and checker[k][l]!=pattern[0][l-j]:
                    w+=1
                if k%2!=0 and checker[k][l]!=pattern[1][l-j]:
                    w+=1
        b=8*8-w
        result.append(min(w,b))
print(min(result))
