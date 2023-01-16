n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 풀이 1
print(sum(a)-sum(b))


# 풀이2
# ans=sum(a)
# idx=0
# for book in b:
#   for i in range(idx,len(b)):
#     if book>b[i]:
#       idx+=1
#     else:
#       ans-=b[i]
#       b[i]-=book
#       break
# print(ans)