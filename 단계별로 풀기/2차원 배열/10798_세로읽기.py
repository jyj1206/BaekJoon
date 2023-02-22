import sys
input = sys.stdin.readline
words = []
for i in range(5):
  words.append(input().strip())

max_length = max(map(len, words))

for col in range(max_length):
  for row in range(5):
    if len(words[row]) <= col:
      continue
    print(words[row][col], end ='')