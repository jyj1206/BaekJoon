d, h, w = map(int,input().split())

h_2=h**2
w_2=w**2

r= d/((h_2+w_2)**0.5)

print(int(h*r),int(w*r))