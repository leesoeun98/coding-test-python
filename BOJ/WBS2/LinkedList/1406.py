import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = []
# stack 두 개 사용
# stack의 top이 커서 역할 => stack1은 커서의 왼쪽, stack2는 커서의 오른쪽
# L이면 stack1.pop을 stack2에 push
# D면 stack2.pop을 stack1에 push
# B면 stack1 pop
# P면 stack1 push
for i in range(int(input())):
    line = sys.stdin.readline().strip()
    if line[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    else:
        stack1.append(line[2])
# 출력시에도 커서의 왼쪽 부분 + 오른쪽 부분 다 더해야 함
print(''.join((stack1 + list(reversed(stack2)))))
