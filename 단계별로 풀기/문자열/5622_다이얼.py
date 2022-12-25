words=input()
dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

sum=0
for word in words:
    for dial in dials:
        if dial.find(word)!=-1:
            break
    sum+=dials.index(dial)+3
print(sum)