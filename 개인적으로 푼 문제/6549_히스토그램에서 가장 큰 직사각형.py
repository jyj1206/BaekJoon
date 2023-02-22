import sys
input = sys.stdin.readline
while True:
  n, *height = map(int, input().split())
  
  if n == 0:
    break
  
  height = list(height)
  
  answer = 0
  stack = []
  for idx, cur_h in enumerate(height):
    # 마지막으로 스택에서 pop한 인덱스 저장
    last = idx
    # 만약에 stack이 있으면서 top이 현재 값보다 큰 경우 계속 pop해 주면서 계산 및 인덱스 저장
    while stack and stack[-1][1] > cur_h:
      i, h = stack.pop()
      answer = max(answer, h * (idx-i))
      last = i
  
    # 스택이 있으면서, stack에 마지막 값이 현재 값하고 같으면 continue
    if stack and stack[-1][1] == cur_h:
      continue
    # 그 외의 경우(스택에 top보다 더 큰 숫자 or 스택이 빈 경우)
    else:
      stack.append((last, cur_h))

  # 남은 스택 처리
  while stack:
    i, h = stack.pop()
    answer = max(answer, h * (n - i))
  
  print(answer)