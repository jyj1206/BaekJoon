n, m = map(int,input().split())
def Euclidian_algorithm(a,b):
    if a%b==0:
        return b
    else : return Euclidian_algorithm(b,a%b)

GCF = Euclidian_algorithm(n,m)
print(GCF)
LCM = n*m//GCF
print(LCM)