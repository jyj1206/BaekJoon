import sys
input = sys.stdin.readline

def rec(s,l,r):
        global count
        count+=1
        if(l>=r) : return 1
        elif (s[l]!=s[r]): return 0
        else : l+=1; r-=1; return rec(s,l,r)

t = int(input())
for i in range(t):
    s = input()
    s=s.strip()
    count=0
    print(rec(s,0,len(s)-1),count)



