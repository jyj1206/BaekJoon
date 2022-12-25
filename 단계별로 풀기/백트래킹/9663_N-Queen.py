import sys
n = int(sys.stdin.readline())
col=[0]*n
def promising(depth):
    for i in range(depth):
        if col[i]==col[depth] or abs(col[i]-col[depth]) == depth-i:
            return False
    return True

def n_queen(depth):
    count=0
    if depth==n:
        return 1
    else :
        for i in range(n):
            col[depth]=i
            if promising(depth):
                count+=n_queen(depth+1)
    return count

print(n_queen(0))