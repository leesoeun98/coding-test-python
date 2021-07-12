from collections import deque
import sys


def bfs(start):
    queue = deque()
    queue.append([start, ""])
    register[start] = 1
    while queue:
        x, d = queue.popleft()
        if x == end:
            return d
        if 2 * x <= 9999 and register[2 * x] == 0:
            register[2 * x] = 1
            queue.append([2 * x, d + 'D'])
        if 2 * x > 9999 and register[(2 * x) % 10000] == 0:
            register[(2 * x) % 10000] = 1
            queue.append([(2 * x) % 10000, d + 'D'])
        if 0 <= x - 1 and register[x - 1] == 0:
            register[x - 1] = 1
            queue.append([x - 1, d + 'S'])
        if 0 > x - 1 and register[9999] == 0:
            register[9999] = 1
            queue.append([9999, d + 'S'])
        nx = int((x % 1000) * 10 + x / 1000)
        if register[nx] == 0:
            register[nx] = 1
            queue.append([nx, d + 'L'])
        nx = int((x % 10) * 1000 + x / 10)
        if register[nx] == 0:
            register[nx] = 1
            queue.append([nx, d + 'R'])


for _ in range(int(input())):
    register = [0] * 10001
    start, end = map(int, sys.stdin.readline().split())
    print(bfs(start))
