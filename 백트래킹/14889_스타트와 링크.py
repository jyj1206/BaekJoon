import sys
input = sys.stdin.readline
n = int(input())

s= [i for i in range(1,n+1)]
ary=[]
for i in range(n):
    ary.append(list(map(int,input().split())))

visited=[False] * n
min_diff=int(2e9)
def func(depth,idx):
    global min_diff
    if depth==n//2:
        team_1=team_2=0
        for i in range(n):
            for j in range(n):
                if i==j: continue
                if visited[i] and visited[j]:
                    team_1+=ary[i][j]
                if not visited[i] and not visited[j]:
                    team_2+=ary[i][j]
        min_diff=min(min_diff,abs(team_1-team_2))
        return

    for i in range(idx,n):
        if visited[i]:
            continue
        visited[i]=True
        func(depth+1,i+1)
        visited[i]=False

func(0,0)
print(min_diff)




# 풀이 2 - 필요없는 연산이 너무 많았음
# team = set([i for i in range(1,n+1)])
# team_A=[]
# ans=[]
# visited=[False]*(n+1)
# def func(start):
#     if len(team_A)==n//2:
#         team_B=list(team-set(team_A))
#         a_sum=b_sum=0
#         for i in range(n//2):
#             for j in range(i,n//2):
#                 a_sum+=ary[team_A[i]-1][team_A[j]-1]+ary[team_A[j]-1][team_A[i]-1]
#                 b_sum+=ary[team_B[i]-1][team_B[j]-1]+ary[team_B[j]-1][team_B[i]-1]
#         ans.append(abs(a_sum-b_sum))
#         return
#     for i in range(start,n+1):
#         if visited[i]:
#             continue
#         visited[i]=True
#         team_A.append(i)
#         func(i+1)
#         team_A.pop()
#         visited[i]=False

# func(1)
# print(min(ans))