n = int(input())
print(n.bit_count())

# bin count
#print(bin(n).count('1'))

# 비트마스킹
# cnt=0
# for i in range(7):
#   if n&(1<<i):
#     cnt+=1
# print(cnt)