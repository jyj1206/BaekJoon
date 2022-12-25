h, m = map(int,input().split())
if m>=45:
    print(f'{h} {m-45}')
else:
    print(f'{(h-1)%24} {m+15}')