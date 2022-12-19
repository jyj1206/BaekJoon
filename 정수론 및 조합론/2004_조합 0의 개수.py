n, m = map(int,input().split())
def cnt_2_or_5(s,t):
    cnt=0
    while s>0:
        cnt+=s//t
        s//=t
    return cnt
cnt_2=cnt_2_or_5(n,2)-cnt_2_or_5(m,2)-cnt_2_or_5(n-m,2)
cnt_5=cnt_2_or_5(n,5)-cnt_2_or_5(m,5)-cnt_2_or_5(n-m,5)
print(min(cnt_2,cnt_5))