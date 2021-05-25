from collections import deque

xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * (m) for _ in range(n)]
queue = deque()


def BFS():
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nearx = x + xd[direction]
            neary = y + yd[direction]
            if 0 <= nearx < n and 0 <= neary < m and tomato[nearx][neary] == 0 and distance[nearx][neary] == 0:
                distance[nearx][neary] = distance[x][y] + 1
                tomato[nearx][neary] = 1
                queue.append((nearx, neary))


for i in range(n):
    for j in range(m):
        if distance[i][j] == 0 and tomato[i][j] == 1:
            queue.append((i, j))
BFS()

flag=True
day=0
for i in range(n):
    day=max(day, max(distance[i]))
    for j in range(m):
        if tomato[i][j]==0:
            flag = False
            break

if flag:
    print(day)
else:
    print(-1)
