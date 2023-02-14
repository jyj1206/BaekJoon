n, k = map(int, input().split())
half_n = n//2
max_k = half_n * (n - half_n)

if k > max_k:
  print(-1)
elif k == max_k:
  print('A' * (n - half_n), end="")
  print('B' * half_n)
else:
  ans = ['B'] * n
  cnt = 0
  Acnt = 0
  
  # 현재 추가 될 수 있는 최대 k
  max_add_k = n - 1
  
  while cnt != k:
    # A가 추가된 수 만큼 cnt 감소
    cnt -= Acnt
    # cnt에 max_add_k를 더 했는데도 k보다 작은 경우, 'A'를 바로 뒤에 넣어줌
    if cnt + max_add_k < k :
      ans[Acnt] = 'A'
      cnt += max_add_k
      max_add_k -= 1  
      Acnt += 1
    else:
      ans[-1 * (k - cnt + 1)] = 'A'
      cnt = k
      
  print(''.join(ans))