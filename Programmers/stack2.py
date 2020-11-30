import math

"""
def solution(progresses, speeds):
    date = [0 for i in range(100)]
    answer = []
    # 1. 각 작업이 끝나는데까지 걸리는 일수
    # 2. 각 작업의 배포 순서 고려
    # 3.
    day = []
    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))

    for i in range(len(day) - 1):
        if day[i] > day[i + 1]:
            day[i + 1] = day[i]

    for i in range(len(day)):
        date[day[i]] += 1

    for i in range(len(date)):
        if date[i] != 0:
            answer.append(date[i])
    return answer
"""


def solution(progresses, speeds):
    answer=[]
    time=0
    count=0
    #1. 진도가 100 넘아가면 count를 1증가
    #2. 진도가 100이 안넘아가면 time을 1증가 (time은 앞의 일이 끝날때까지 시간 버는거니까 누적),
    # 가장 배포 우선 되는 애가 끝나야 해당 원소가 pop

    while len(progresses)>0:
        if progresses[0]+(time*speeds[0])>=100:
            print(progresses[0])
            progresses.pop(0)
            speeds.pop(0)
            count+=1
            print(count, time)
        else:
            if count>0:
                # 맨 마지막 count만 append됨
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    return answer
