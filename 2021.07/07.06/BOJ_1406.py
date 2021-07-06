import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = []
for _ in range(int(input())):
    command = sys.stdin.readline().strip()
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    else:
        stack1.append(command[2])
print(''.join((stack1 + list(reversed(stack2)))))
