import sys
input = sys.stdin.readline
n = int(input())
class_room=[[set() for j in range(10)] for i in range(5)]

students=[]
for i in range(n):
  student=list(map(int,input().split()))
  students.append(student)
  for j in range(5):
    class_room[j][student[j]].add(i)

max_cnt=-int(1e9)
for i in range(n):
  cnt=set()
  for j in range(5):
    cnt|=class_room[j][students[i][j]]
  if max_cnt<len(cnt)-1:
      max_cnt=len(cnt)-1
      ans=i

print(ans+1)