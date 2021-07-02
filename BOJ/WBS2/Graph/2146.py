import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
res=sys.maxsize

# 섬 라벨링
def dfs(i, j):
    for d in range(4):
        nearx = x[d] + i
        neary = y[d] + j
        if 0 <= nearx < n and 0 <= neary < n and visited[nearx][neary] == 0 and graph[nearx][neary] == 1:
            graph[nearx][neary] = cnt
            visited[nearx][neary] = 1
            dfs(nearx, neary)

def bfs(idx):
    global res
    dist=[[-1]*n for _ in range(n)]
    queue=deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j]==idx:
              queue.append((i, j))
              dist[i][j]=0

    while queue:
        curx, cury=queue.popleft()
        for d in range(4):
            nearx=curx+x[d]
            neary=cury+y[d]
            if 0<=nearx<n and 0<=neary<n:
                # 다른 섬 도착
                if graph[nearx][neary]>0 and graph[nearx][neary]!=idx:
                    res=min(res, dist[curx][cury])
                    return
                # 바다, 간척 안된 곳이면 간척
                if graph[nearx][neary]==0 and dist[nearx][neary]==-1:
                    dist[nearx][neary]=dist[curx][cury]+1
                    queue.append((nearx, neary))

# 섬 라벨링
cnt = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i, j)
            cnt += 1
# 섬 간척
for i in range(1, cnt):
    bfs(i)
print(res)

