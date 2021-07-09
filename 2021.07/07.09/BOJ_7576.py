from collections import deque
m, n = map(int, input().split())
tomato=[list(map(int, input().split())) for _ in range(n)]
distance=[[0]*m for _ in range(n)]
queue=deque()
xd=[-1,1,0,0]
yd=[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nearx=x+xd[d]
        neary=y+yd[d]
        if 0<=nearx<n and 0<=neary<m and distance[nearx][neary]==0 and tomato[nearx][neary]==0:
            tomato[nearx][neary]=1
            distance[nearx][neary]=distance[x][y]+1
            queue.append((nearx, neary))
flag=True
for i in range(n):
    for j in range(m):
        if tomato[i][j]==0:
            flag=False
            break
day=0
for line in distance:
    day=max(day, max(line))
if flag:
    print(day)
else:
    print(-1)