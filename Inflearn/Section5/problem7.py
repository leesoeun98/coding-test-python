from collections import deque

need = input()
for _ in range(int(input())):
    needs = deque(need)
    schedule = deque()
    course = input()
    for c in course:
        # 하나씩만 저장
        if c in need and c not in schedule:
            schedule.append(c)
    while schedule and need:
        if schedule.popleft() != needs.popleft():
            print("NO")
            break
    else:
        # 하나씩만 담아서 schedule은 needs보다 작거나 같음
        if len(needs) != 0:
            print("NO")
        else:
            print("YES")
