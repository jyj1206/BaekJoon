import sys
input = sys.stdin.readline
# 숫자 갯수
n = int(input())
# 수열
num = list(map(int,input().split()))
# 연산자 종류
operator=['+','-','*','%']
# 각 연산자 갯수
operator_num=list(map(int,input().split()))

ans=[]
def cal(result):
    temp=num[0]
    for i in range(n-1):
        opr=result[i]
        if opr=='+': temp+=num[i+1]
        elif opr == '-': temp-=num[i+1]
        elif opr == '*': temp*=num[i+1]
        else : 
            if temp<0 : temp = -1*((temp*-1)//num[i+1])
            else : temp//=num[i+1]
    ans.append(temp)

result=[]
def func(depth):
    if depth==n-1:
            cal(result)
            return
    for i in range(4):
        if operator_num[i]==0:
            continue
        operator_num[i]-=1
        result.append(operator[i])
        func(depth+1)
        result.pop()
        operator_num[i]+=1

func(0)
print(max(ans))
print(min(ans))