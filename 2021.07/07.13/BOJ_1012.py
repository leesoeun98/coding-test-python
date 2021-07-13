import sys

sys.setrecursionlimit(10 ** 6)
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]


def dfs(i, j):
    for d in range(4):
        nearx = i + xd[d]
        neary = j + yd[d]
        if 0 <= nearx < n and 0 <= neary < m and garden[nearx][neary] == 1:
            garden[nearx][neary] = idx
            dfs(nearx, neary)


for _ in range(int(input())):
    idx = 2
    cnt = 0
    m, n, k = map(int, input().split())
    garden = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        garden[y][x] = 1

    for i in range(n):
        for j in range(m):
            if garden[i][j] == 1:
                dfs(i, j)
                idx += 1
                cnt += 1
    print(cnt)
