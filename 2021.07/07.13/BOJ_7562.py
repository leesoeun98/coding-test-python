from collections import deque
xd = [-2, -1, 1, 2, 2, 1, -1, -2]
yd = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(int(input())):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    distance=[[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    queue=deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        if x==ex and y==ey:
            break
        for d in range(8):
            nearx = x+xd[d]
            neary=y+yd[d]
            if 0<=nearx<l and 0<=neary<l and distance[nearx][neary]==0:
                distance[nearx][neary]=distance[x][y]+1
                queue.append((nearx, neary))
    print(distance[ex][ey])

