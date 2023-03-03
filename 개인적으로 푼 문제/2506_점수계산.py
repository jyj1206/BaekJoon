n = int(input())
correct = list(map(int, input().split()))

point = [0] * n

point[0] = correct[0]

for i in range(1, n):
  if correct[i] == 1:
      point[i] = 1
      point[i] += point[i-1]

print(sum(point))