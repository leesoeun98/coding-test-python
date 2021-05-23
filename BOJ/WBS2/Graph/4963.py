import sys
sys.setrecursionlimit(2500) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
xd = [0, 1, 1, 1, 0, -1, -1, -1]
yd = [1, 1, 0, -1, -1, -1, 0, 1]


def DFS(i, j):
    visited[i][j] = 1
    for direction in range(8):
        x = i + xd[direction]
        y = j + yd[direction]
        if 0 <= x < h and 0 <= y < w and visited[x][y] == 0 and maps[x][y] == 1:
            DFS(x, y)
            visited[x][y] = 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * (w) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and maps[i][j] == 1:
                DFS(i, j)
                count += 1
    print(count)
