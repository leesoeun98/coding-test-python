from collections import deque
board=[list(map(int, input().split())) for _ in range(7)]
distance=[[0]*7 for _ in range(7)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]
queue=deque()
queue.append((0,0))
while queue:
    x, y = queue.popleft()
    for d in range(4):
        nearx = x+xd[d]
        neary=y+yd[d]
        if 0<=nearx<7 and 0<=neary<7 and board[nearx][neary]==0:
            board[nearx][neary]=1
            distance[nearx][neary]=distance[x][y]+1
            queue.append((nearx, neary))
if distance[6][6]==0:
    print(-1)
else:
    print(distance[6][6])
