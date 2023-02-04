burger=[int(input()) for _ in range(3)]
coke=int(input())
cider=int(input())

print(min(burger)+min(coke,cider)-50)