d, h, w = map(int,input().split())

h_2=h**2
w_2=w**2

ans_h= (h*d)/((h_2+w_2)**(1/2))

ans_w= (w*d)/((h_2+w_2)**(1/2))

print(int(ans_h),int(ans_w))