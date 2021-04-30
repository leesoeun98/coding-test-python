from collections import deque

n = int(input())
num = list(map(int, input().split()))
num = deque(num)
answer = []
res=""
while num:
    if len(answer) == 0:
        if num[0] < num[-1]:
            answer.append((num.popleft(), 'L'))
        else:
            answer.append((num.pop(), 'R'))
    else:
        if num[0] < num[-1]:
            if answer[-1][0] < num[0]:
                answer.append((num.popleft(), 'L'))
            elif answer[-1][0] < num[-1]:
                answer.append((num.pop(), 'R'))
            else:
                break
        else:
            if answer[-1][0] < num[-1]:
                answer.append((num.pop(), 'R'))
            elif answer[-1][0] < num[0]:
                answer.append((num.popleft(), 'L'))
            else:
                break
print(answer)
for a in answer:
    res+=a[1]
print(res)
