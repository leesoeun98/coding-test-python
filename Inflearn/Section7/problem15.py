from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(n)]
distance = [[0] * m for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
queue = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nearx = x + xd[d]
        neary = y + yd[d]
        if 0 <= nearx < n and 0 <= neary < m and distance[nearx][neary] == 0 and tomato[nearx][neary] == 0:
            distance[nearx][neary] = distance[x][y] + 1
            tomato[nearx][neary]=1
            queue.append((nearx, neary))

flag = 0
res=0
for i in range(n):
    for j in range(m):
        if tomato[i][j]==0:
            flag=1
if flag==1:
    print(-1)
else:
    for i in range(n):
        res=max(res, max(distance[i]))
    print(res)