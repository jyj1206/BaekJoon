month=[31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week=['MON','TUE','WED','THU','FRI','SAT','SUN']
x,y = map(int,input().split())
month_diff=x-1
day=y-1

for i in range(month_diff):
  day+=month[i]

print(day_of_week[day%7])