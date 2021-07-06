from collections import deque
x=[-1,1,0,0]
y=[0,0,-1,1]

w, h = map(int,input().split())
board=[list(map(int, input().split())) for _ in range(h)]
distance=[[0]*w for _ in range(h)]
queue=deque()
for i in range(h):
    for j in range(w):
        if board[i][j]==1:
            queue.append((i, j))

while queue:
    curx, cury=queue.popleft()
    for d in range(4):
        nearx=x[d]+curx
        neary=y[d]+cury
        if 0<=nearx<h and 0<=neary<w and board[nearx][neary]==0 and distance[nearx][neary]==0:
            distance[nearx][neary]=distance[curx][cury]+1
            board[nearx][neary]=1
            queue.append((nearx, neary))
day=0
flag=True
for i in range(h):
    for j in range(w):
        if board[i][j]==0:
            flag=False
            break
for line in distance:
    day=max(day, max(line))

if flag:
    print(day)
else:
    print(-1)
