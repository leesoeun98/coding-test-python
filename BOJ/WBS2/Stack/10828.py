import sys
stack = []
#표준입출력시 시간초과

def push(x):
    stack.append(x)


def top():
    if stack:
        return stack[-1]
    else:
        return -1


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1


for _ in range(int(input())):
    input_split = sys.stdin.readline().rstrip().split()

    cmd = input_split[0]
    if 'push' in cmd:
        push(int(input_split[1]))
    elif cmd == 'top':
        print(top())
    elif cmd == 'size':
        print(size())
    elif cmd == 'empty':
        empty()
    else:
        print(pop())
