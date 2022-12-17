import sys
input = sys.stdin.readline
def is_div_or_mul(a,b):
    if a%b==0:
        print('multiple')
    elif b%a==0:
        print('factor')
    else:
        print('neither')

while(True):
    a, b= map(int,input().split())
    if a==b==0:
        break
    is_div_or_mul(a,b)

