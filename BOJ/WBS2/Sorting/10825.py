#표준 입출력 시 시간초과 
import sys
student=[]
for _ in range(int(input())):
    name, korean, english, math = sys.stdin.readline().split()
    student.append((name, int(korean), int(english), int(math)))
student.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(len(student)):
    print(student[i][0])