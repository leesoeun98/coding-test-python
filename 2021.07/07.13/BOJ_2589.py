from collections import deque
import sys
l, w = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(l)]

xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
res = 0
queue = deque()

def bfs(i, j):
    queue.append((i, j))
    distance = [[-1] * w for _ in range(l)]
    distance[i][j] = 0
    maxn = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nearx = x + xd[d]
            neary = y + yd[d]
            if 0 <= nearx < l and 0 <= neary < w and board[nearx][neary] == 'L' and distance[nearx][neary] == -1:
                distance[nearx][neary] = distance[x][y] + 1
                maxn = max(maxn, distance[nearx][neary])
                queue.append((nearx, neary))

    return maxn


for i in range(l):
    for j in range(w):
        if board[i][j] == 'L':
            res = max(res, bfs(i, j))
print(res)
