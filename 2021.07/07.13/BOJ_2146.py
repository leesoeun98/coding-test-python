from collections import deque
import sys
sys.setrecursionlimit(10**6)
n = int(input())
board=[list(map(int, input().split())) for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]

# dfs로 섬 라벨링
def dfs(i, j):
    for d in range(4):
        nearx = i+xd[d]
        neary = j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==1:
            board[nearx][neary]=idx
            dfs(nearx, neary)
idx=2

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=idx
            dfs(i, j)
            idx+=1

res=987654321
# bfs로 간척

def bfs(idx):
    global res
    queue=deque()
    distance=[[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j]==idx:
                queue.append((i, j))
                distance[i][j]=0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x+xd[d]
            ny = y+yd[d]
            #바다먄 간척
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0 and distance[nx][ny]==-1:
                distance[nx][ny]=distance[x][y]+1
                queue.append((nx, ny))
            #다른 섬 도착
            elif 0<=nx<n and 0<=ny<n and board[nx][ny]>0 and board[nx][ny]!=idx:
                res=min(res, distance[x][y])
                return


for i in range(2, idx):
    bfs(i)
print(res)