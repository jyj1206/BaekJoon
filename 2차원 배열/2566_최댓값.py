a=[]
max_num=0
max_index=(1,1)
for i in range(9):
    row=list(map(int,input().split()))
    if max(row)>max_num:
        max_num=max(row)
        max_index = (i+1,row.index(max_num)+1)
    a.append(row)

print(max_num)
print(max_index[0],max_index[1])