from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
distance[0][0]=1
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nearx = x + xd[d]
        neary = y + yd[d]
        if 0 <= nearx < n and 0 <= neary < m and board[nearx][neary] == 1 and distance[nearx][neary] == 0:
            distance[nearx][neary] = distance[x][y] + 1
            board[nearx][neary]=0
            queue.append((nearx, neary))

print(distance[n - 1][m - 1])
