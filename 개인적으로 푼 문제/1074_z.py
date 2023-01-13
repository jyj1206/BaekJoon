n,r,c = map(int,input().split())
z=[(0,0,0),(0,1,1),(1,0,2),(1,1,3)]
cnt=0

def z_find(i,j,size,num):
  if size==2:
    for case in z:
      if i+case[0]==r and j+case[1]==c:
        print(num+case[2])
        return
  else:
    size=size//2
    if i<=r<i+size and j<=c<j+size:
      z_find(i,j,size,num)
    elif i<=r<i+size :
      z_find(i,j+size,size,num+(size**2)*1)
    elif j<=c<j+size:
      z_find(i+size,j,size,num+(size**2)*2)
    else:
      z_find(i+size,j+size,size,num+(size**2)*3)

z_find(0,0,2**n,0)








# 시간초과
# _dict={}
# def z_marking(i,j,size):
#   global cnt
#   if size==2:
#     for t in z:
#       x=t[0]
#       y=t[1]
#       _dict[(i+x),(j+y)]=cnt
#       cnt+=1
#   else:
#     size=size//2
#     z_marking(i,j,size)
#     z_marking(i,j+size,size)
#     z_marking(i+size,j,size)
#     z_marking(i+size,j+size,size)

# z_marking(0,0,2**n)

# print(_dict[r,c])