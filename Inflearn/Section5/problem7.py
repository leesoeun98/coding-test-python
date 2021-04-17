#1차 시도 실패 (답안 봄...근데 이해 잘 못함) => 초기화 주의
from collections import deque
need=input()
for i in range(int(input())):
    mandatory = deque(need)
    curi=input()
    check=deque()
    for c in curi:
        if c in mandatory and c not in check:
            check.append(c)
    if len(check)==0:
        print("NO")
        exit(0)
    while mandatory and check:
        if check.popleft()!=mandatory.popleft():
            print("NO")
            break
    else:
        if len(mandatory)==0:
            print("YES")
        else:
            print("NO")

"""
from collections import deque
need = input()
for i in range(int(input())):
    course = input()
    needs=deque(need)
    schedule = deque()
    # course의 각 수업이 needs에 포함되어 있고, 동일하다면 pop
    for c in course:
        # 1개씩만 순서대로 담음
        if c in needs and c not in schedule:
            schedule.append(c)
    if len(schedule)==0:
        print("NO")
        exit(0)
    while needs and schedule:
        if needs.popleft()!=schedule.popleft():
            print("NO")
            break
    else:
        #schedule이 더 적었다면 needs가 남을 것.
        #반대의 경우는 있을 수 없음 (1개씩만 저장하므로 길이가 같거나 적은 경우만 존재)
        if len(needs)==0:
            print("YES")
        else:
            print("NO")
"""