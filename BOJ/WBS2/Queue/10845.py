from collections import deque
import sys
queue = deque()
for i in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        queue.append(int(cmd[5:]))
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
