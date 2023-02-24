n = int(input())
f = input()

num = []
oper = []

def calc(num1, num2, oper):
  if oper == '+':
    return num1 + num2
  elif oper == '-':
    return num1 - num2
  else:
    return num1 * num2
  
for i in range(n):
  if i%2==0:
    num.append(int(f[i]))
  else:
    oper.append(f[i])

INF = int(1e10)
result = - INF

def dfs(idx, value):
  global result
  if idx == len(oper):
    result = max(result, value)
    return
  
  if idx + 1 <= len(oper):
    dfs(idx + 1, calc(value, num[idx + 1], oper[idx]))
  if idx + 2 <= len(oper):
    dfs(idx + 2, calc(value, calc(num[idx + 1], num[idx + 2], oper[idx + 1]), oper[idx]))
    
dfs(0, num[0])
print(result)