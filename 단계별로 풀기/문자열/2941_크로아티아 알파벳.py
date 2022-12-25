c_alpas=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
sum=0
for c_alpa in c_alpas:
    sum+=word.count(c_alpa)
    
print(len(word)-sum)
