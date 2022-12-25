n=int(input())
ans=[]
def hanoi(n,from_pos,to_pos,by_pos):
    if n==1:
        print(from_pos, to_pos)
        return
    hanoi(n-1,from_pos,by_pos,to_pos)    
    print(from_pos,to_pos)
    hanoi(n-1,by_pos,to_pos,from_pos)

#print(2**n-1)
count=0
for i in range(n):
    count=2*count+1
print(count)
hanoi(n,1,3,2) 

