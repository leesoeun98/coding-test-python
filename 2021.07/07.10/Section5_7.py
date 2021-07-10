from collections import deque
needs=list(input())
for _ in range(int(input())):
    schedule=list(input())
    need=deque(needs)
    order=deque()
    flag=True
    for s in schedule:
        if s in need and s not in order:
            order.append(s)
    #schedule은 need랑 길이 같거나 짧음
    while order:
        if need.pop()!=order.pop():
            print("NO")
            break
    else:
        if len(need)==0:
            print("YES")
        else:
            print("NO")

