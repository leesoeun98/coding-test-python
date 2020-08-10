import sys
num=int(input())
people=[]
idx=0
for _ in range(num):
    age, name=sys.stdin.readline().strip().split()
    #가입순, 나이, 이름을 list에 저장, 단 int로 하기
    people.append([idx, int(age), name])
    idx+=1
#나이순으로 먼저 정렬 후, 가입순으로 정렬
people=sorted(people, key=lambda person: (person[1]))

for person in people:
    print(person[1], person[2])

