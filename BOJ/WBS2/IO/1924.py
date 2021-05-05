month, day = map(int, input().split())
perday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date=["SUN","MON","TUE","WED","THU","FRI","SAT"]
total=0
for i in range(month-1):
    total+=perday[i]
total+=day
print(date[total%7])