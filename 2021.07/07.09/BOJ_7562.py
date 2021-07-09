from collections import deque
xd = [1, 2, 2, 1, -1, -2, -2, -1]
yd = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited=[[0]*n for _ in range(n)]
    queue=deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        if x==ex and y==ey:
            break
        for d in range(8):
            nearx=x+xd[d]
            neary=y+yd[d]
            if 0<=nearx<n and 0<=neary<n and visited[nearx][neary]==0:
                visited[nearx][neary]=visited[x][y]+1
                queue.append((nearx, neary))
    print(visited[ex][ey])


