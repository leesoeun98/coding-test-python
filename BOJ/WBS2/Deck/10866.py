from collections import deque
import sys
queue = deque()
for i in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:9] == 'push_back':
        queue.append(int(cmd[10:]))
    elif cmd[:10]=='push_front':
        queue.appendleft(int(cmd[11:]))
    elif cmd[:10] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[:9]=='pop_back':
        if queue:
            print(queue.pop())
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
