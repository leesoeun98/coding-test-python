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


