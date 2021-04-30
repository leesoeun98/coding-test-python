from collections import deque

need = input()
for _ in range(int(input())):
    schedule = input()
    needs = deque(need)
    check = []
    check = deque(check)
    for s in schedule:
        if s in need and s not in check:
            check.append(s)
    # check는 항상 need보다 짧거나 길이 같음
    while check:
        if needs.popleft() != check.popleft():
            print("NO")
            break
    else:
        if len(needs) == 0:
            print("YES")
        else:
            print("NO")
